from gi.repository import Gtk, Gio, Gdk

css_file = Gio.File.new_for_path("./css/main.css")

class MainWindow(Gtk.ApplicationWindow):
    def __init__(self, start_screen, *args, **kwargs):
        super().__init__(*args, **kwargs)

        screen = Gdk.Screen.get_default()
        provider = Gtk.CssProvider()
        style_context = Gtk.StyleContext()
        style_context.add_provider_for_screen(screen, provider, Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)
        provider.load_from_file(css_file)
        self.current_screen = start_screen(self.change_screen)
        self.add(self.current_screen)
        self.current_screen.show()
        
    def change_screen(self, screen):
        self.remove(self.current_screen)
        self.current_screen.destroy()
        self.current_screen = screen(self.change_screen)
        self.add(self.current_screen)
        self.current_screen.show()
	