
import pystray
from PIL import Image, ImageDraw
import threading
import time
import json
import tkinter as tk
from tkinter import simpledialog, messagebox
import os
from plyer import notification
from monitor import WebsiteMonitor

SETTINGS_FILE = 'settings.json'
URL_FILE = '지역교육청_url.txt'

class ProgressWindow:
    def __init__(self, monitor, on_close_callback, master):
        self.monitor = monitor
        self.on_close_callback = on_close_callback
        self.window = tk.Toplevel(master) # Use Toplevel instead of Tk
        self.window.title("EduMonitor Checking...")
        self.window.geometry("400x500")
        self.window.attributes('-topmost', True)
        
        # Center the window
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()
        x = (screen_width - 400) // 2
        y = (screen_height - 500) // 2
        self.window.geometry(f"400x500+{x}+{y}")

        self.listbox = tk.Listbox(self.window, width=50, height=25)
        self.listbox.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)
        
        self.status_label = tk.Label(self.window, text="Preparing...", fg="blue")
        self.status_label.pack(pady=5)

        self.urls = self.monitor.get_urls()
        self.failed_sites = []
        self.network_error = False
        
        # Start checking automatically
        self.window.after(100, self.start_check)
        self.window.protocol("WM_DELETE_WINDOW", self.on_close)

    def start_check(self):
        threading.Thread(target=self.run_check_process, daemon=True).start()

    def run_check_process(self):
        # 1. Check Network
        self.update_status("Checking Network...", "blue")
        if not self.monitor.check_network():
            self.network_error = True
            self.update_status("Network Error!", "red")
            self.add_log("Network: FAIL (Ping 8.8.8.8)")
            self.finish_check()
            return

        self.add_log("Network: OK")
        
        # 2. Check Sites
        total = len(self.urls)
        for i, (name, url) in enumerate(self.urls.items()):
            self.update_status(f"Checking {name} ({i+1}/{total})...", "black")
            success, error = self.monitor.check_site(url)
            
            if success:
                self.add_log(f"[OK] {name} - {url}")
            else:
                self.add_log(f"[FAIL] {name} - {url} - {error}")
                self.failed_sites.append({'name': name, 'url': url, 'error': error})
        
        self.finish_check()

    def update_status(self, text, color):
        try:
            self.window.after(0, lambda: self.status_label.config(text=text, fg=color))
        except:
            pass

    def add_log(self, text):
        try:
            self.window.after(0, lambda: self.listbox.insert(tk.END, text))
            self.window.after(0, lambda: self.listbox.see(tk.END))
        except:
            pass

    def finish_check(self):
        if self.network_error or self.failed_sites:
            self.update_status("Check Completed: Issues Found", "red")
            result = {'network_error': self.network_error, 'failed_sites': self.failed_sites}
        else:
            self.update_status("Check Completed: All Good", "green")
            result = {'network_error': False, 'failed_sites': []}
            # Auto close after 2 seconds if success
            try:
                self.window.after(2000, self.on_close)
            except:
                pass
        
        self.on_close_callback(result)

    def on_close(self):
        try:
            self.window.destroy()
        except:
            pass

class TrayApp:
    def __init__(self):
        self.monitor = WebsiteMonitor()
        self.load_settings()
        self.icon = None
        self.running = True
        self.monitor.load_urls(URL_FILE)
        
        # Main root window (hidden)
        self.root = tk.Tk()
        self.root.withdraw()

    def load_settings(self):
        if os.path.exists(SETTINGS_FILE):
            try:
                with open(SETTINGS_FILE, 'r') as f:
                    self.settings = json.load(f)
            except:
                self.settings = {}
        else:
            self.settings = {}
        
        # Set defaults
        if 'interval_minutes' not in self.settings:
            self.settings['interval_minutes'] = 10
        if 'show_popup' not in self.settings:
            self.settings['show_popup'] = True
            
        self.save_settings()

    def save_settings(self):
        with open(SETTINGS_FILE, 'w') as f:
            json.dump(self.settings, f, indent=4)

    def create_image(self, color):
        width = 64
        height = 64
        image = Image.new('RGB', (width, height), color)
        dc = ImageDraw.Draw(image)
        dc.rectangle((0, 0, width, height), fill=color)
        return image

    def run_scheduler(self):
        # Initial Check (wait a bit for UI to be ready)
        time.sleep(2)
        self.trigger_check()
        
        last_check_time = time.time()
        
        while self.running:
            interval_sec = self.settings.get('interval_minutes', 10) * 60
            
            if time.time() - last_check_time >= interval_sec:
                self.trigger_check()
                last_check_time = time.time()
            
            time.sleep(1)

    def trigger_check(self):
        # Dispatch check to Main Thread if needed
        # We use root.after to safely trigger UI stuff
        self.root.after(0, self.check_websites)

    def check_websites(self):
        if self.settings.get('show_popup', True):
            # Run with GUI
            self.run_popup_check()
        else:
            # Run silently in a separate thread to avoid freezing GUI
            threading.Thread(target=self.run_silent_check, daemon=True).start()

    def run_silent_check(self):
        result = self.monitor.run_check()
        self.handle_check_result(result)

    def run_popup_check(self):
        # Callback wrapper to bridge GUI result back to logic
        def callback(result):
            self.handle_check_result(result)
            
        # Create ProgressWindow
        ProgressWindow(self.monitor, callback, self.root)

    def handle_check_result(self, result):
        if result['network_error']:
            self.update_icon('red')
            self.show_notification("Network Error", "Cannot connect to the internet.")
        elif result['failed_sites']:
            self.update_icon('red')
            failed_names = ", ".join([site['name'] for site in result['failed_sites']])
            self.show_notification("Website Failure", f"Failed: {failed_names}")
        else:
            self.update_icon('green')

    def update_icon(self, color):
        if self.icon:
            # Icon update is usually thread-safe or handled by library, 
            # but to be safe we can wrap it if needed. 
            # pystray doesn't have an 'after', so we assume it handles it or we call it directly.
            self.icon.icon = self.create_image(color)

    def show_notification(self, title, message):
        try:
            notification.notify(
                title=title,
                message=message,
                app_name='EduMonitor',
                timeout=10
            )
        except Exception:
            pass

    def on_check_now(self, icon, item):
        self.trigger_check()

    def on_settings(self, icon, item):
        # Dispatch to Main Thread
        self.root.after(0, self.show_settings_dialog)

    def show_settings_dialog(self):
        # Create a Settings Dialog using Toplevel
        win = tk.Toplevel(self.root)
        win.title("Settings")
        
        # Center
        screen_width = win.winfo_screenwidth()
        screen_height = win.winfo_screenheight()
        x = (screen_width - 350) // 2
        y = (screen_height - 250) // 2
        win.geometry(f"350x250+{x}+{y}")
        win.attributes('-topmost', True)

        # Interval
        tk.Label(win, text="Check Interval (minutes):").pack(pady=10)
        interval_var = tk.IntVar(value=self.settings.get('interval_minutes', 10))
        tk.Entry(win, textvariable=interval_var).pack()

        # Popup Toggle
        popup_var = tk.BooleanVar(value=self.settings.get('show_popup', True))
        tk.Checkbutton(win, text="Show Check Progress Popup\n(체크리스트 진행 상황 조회)", variable=popup_var).pack(pady=10)

        def save():
            self.settings['interval_minutes'] = interval_var.get()
            self.settings['show_popup'] = popup_var.get()
            self.save_settings()
            win.destroy()

        tk.Button(win, text="Save", command=save).pack(pady=20)

    def on_exit(self, icon, item):
        self.running = False
        self.icon.stop()
        self.root.quit()
        # Ensure we really exit
        os._exit(0)

    def run_icon_thread(self):
        image = self.create_image('green')
        menu = pystray.Menu(
            pystray.MenuItem("Check Now", self.on_check_now),
            pystray.MenuItem("Settings", self.on_settings),
            pystray.MenuItem("Exit", self.on_exit)
        )
        self.icon = pystray.Icon("EduMonitor", image, "EduMonitor", menu)
        self.icon.run()

    def run(self):
        # Start scheduler in background
        threading.Thread(target=self.run_scheduler, daemon=True).start()
        
        # Start Icon in background
        threading.Thread(target=self.run_icon_thread, daemon=True).start()
        
        # Run Tkinter Mainloop (Blocking Main Thread)
        self.root.mainloop()

if __name__ == "__main__":
    app = TrayApp()
    app.run()
