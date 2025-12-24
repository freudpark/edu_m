
import flet as ft
from monitor import WebsiteMonitor
import threading
import time

URL_FILE = '지역교육청_url.txt'

class EduMonitorApp:
    def __init__(self, page: ft.Page):
        self.page = page
        self.page.title = "EduMonitor Mobile"
        self.page.theme_mode = ft.ThemeMode.SYSTEM
        self.page.scroll = "adaptive"
        # Mobile-like sizing for desktop preview
        self.page.window.width = 375
        self.page.window.height = 700
        
        self.monitor = WebsiteMonitor()
        self.monitor.load_urls(URL_FILE)
        
        self.init_ui()

    def init_ui(self):
        # --- App Bar ---
        self.page.appbar = ft.AppBar(
            title=ft.Text("EduMonitor"),
            center_title=True,
            bgcolor=ft.Colors.BLUE_GREY_100,
            actions=[
                ft.IconButton(ft.Icons.SETTINGS, on_click=self.go_to_settings)
            ]
        )

        # --- Main List ---
        self.site_list_view = ft.ListView(expand=1, spacing=10, padding=20)
        self.load_sites_into_list()
        
        # --- Loading Indicator (Hidden by default) ---
        self.progress_ring = ft.ProgressRing(visible=False)
        self.status_text = ft.Text("", color=ft.Colors.GREY)

        # --- FAB ---
        self.check_fab = ft.FloatingActionButton(
            icon=ft.Icons.REFRESH,
            text="Check Now",
            on_click=self.start_check_thread
        )

        # --- Layout ---
        self.page.add(
            ft.Column(
                [
                    ft.Container(self.status_text, alignment=ft.alignment.center),
                    ft.Container(self.progress_ring, alignment=ft.alignment.center),
                    self.site_list_view,
                ],
                expand=True
            )
        )
        self.page.floating_action_button = self.check_fab

    def load_sites_into_list(self):
        self.site_list_view.controls.clear()
        urls = self.monitor.get_urls()
        
        if not urls:
            self.site_list_view.controls.append(ft.Text("No URLs found.", text_align="center"))
            return

        for name, url in urls.items():
            card = ft.Card(
                content=ft.Container(
                    content=ft.Column(
                        [
                            ft.ListTile(
                                leading=ft.Icon(ft.Icons.CIRCLE_OUTLINED, color=ft.Colors.GREY),
                                title=ft.Text(name, weight="bold"),
                                subtitle=ft.Text(url, max_lines=1, overflow=ft.TextOverflow.ELLIPSIS),
                            )
                        ]
                    ),
                    padding=10,
                ),
                data=url # Store URL in data for easier access if needed
            )
            self.site_list_view.controls.append(card)
        
        self.page.update()

    def start_check_thread(self, e):
        if self.progress_ring.visible:
            return  # Already checking
        
        self.progress_ring.visible = True
        self.check_fab.disabled = True
        self.status_text.value = "Checking Network..."
        self.page.update()
        
        threading.Thread(target=self.run_check, daemon=True).start()

    def run_check(self):
        # 1. Network Check
        is_net_ok = self.monitor.check_network()
        if not is_net_ok:
            self.finish_check("Network Error", False, [])
            return

        self.update_status_safe("Checking Sites...")

        # 2. Check Sites
        urls = self.monitor.get_urls()
        total = len(urls)
        failed_sites = []
        
        # Reset icons to loading
        for control in self.site_list_view.controls:
             if isinstance(control, ft.Card):
                tile = control.content.content.controls[0]
                tile.leading.name = ft.Icons.HOURGLASS_EMPTY
                tile.leading.color = ft.Colors.BLUE
        self.page.update()

        for i, (name, url) in enumerate(urls.items()):
            # Find the card for this site
            card = None
            for c in self.site_list_view.controls:
                if isinstance(c, ft.Card) and c.data == url:
                    card = c
                    break
            
            success, error = self.monitor.check_site(url)
            
            # Update individual item
            if card:
                tile = card.content.content.controls[0]
                if success:
                    tile.leading.name = ft.Icons.CHECK_CIRCLE
                    tile.leading.color = ft.Colors.GREEN
                else:
                    tile.leading.name = ft.Icons.ERROR
                    tile.leading.color = ft.Colors.RED
                    failed_sites.append({'name': name, 'error': error})
                self.page.update()
        
        if failed_sites:
            self.finish_check("Issues Found", False, failed_sites)
        else:
            self.finish_check("All Good", True, [])

    def update_status_safe(self, text):
        self.status_text.value = text
        self.page.update()

    def finish_check(self, msg, success, failures):
        self.progress_ring.visible = False
        self.check_fab.disabled = False
        self.status_text.value = msg
        self.status_text.color = ft.Colors.GREEN if success else ft.Colors.RED
        
        if failures:
             self.page.show_snack_bar(ft.SnackBar(content=ft.Text(f"Failed: {len(failures)} sites")))
        
        self.page.update()

    def go_to_settings(self, e):
        # We can simulate navigation or open a dialog
        # For simplicity in this one-page app, let's show a bottom sheet or dialog
        def close_dlg(e):
            self.page.dialog.open = False
            self.page.update()

        dlg = ft.AlertDialog(
            title=ft.Text("Settings"),
            content=ft.Text("Settings are not implemented in this demo Mobile UI."),
            actions=[
                ft.TextButton("Close", on_click=close_dlg)
            ],
            actions_alignment=ft.MainAxisAlignment.END,
        )
        self.page.dialog = dlg
        dlg.open = True
        self.page.update()

def main(page: ft.Page):
    app = EduMonitorApp(page)

if __name__ == "__main__":
    ft.app(target=main)
