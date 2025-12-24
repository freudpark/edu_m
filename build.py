
import PyInstaller.__main__
import os

def build():
    PyInstaller.__main__.run([
        'tray_app.py',
        '--onefile',
        '--noconsole',
        '--name=EduMonitor',
        '--clean',
        '--hidden-import=plyer.platforms.win.notification',
    ])

if __name__ == "__main__":
    build()
