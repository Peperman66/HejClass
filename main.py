import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from windows.MainWindow import MainWindow
from screens import OnScreen

class Application(Gtk.Application):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, application_id="org.hejclass", **kwargs)
        
        self.window = None
        
    def do_startup(self):
        Gtk.Application.do_startup(self)
    
    def do_activate(self):
        if not self.window:
            self.window = MainWindow(OnScreen, application=self, title="HejClass")

        self.window.present()
        self.window.fullscreen()

if __name__ == "__main__":
    app = Application()
    app.run()
    