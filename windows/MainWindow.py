from gi.repository import Gtk

class MainWindow(Gtk.ApplicationWindow):
    def __init__(self, start_screen, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.current_screen = start_screen(self.change_screen)
        self.add(self.current_screen)
        self.current_screen.show()
        
    def change_screen(self, screen):
        self.remove(self.current_screen)
        self.current_screen.destroy()
        self.current_screen = screen(self.change_screen)
        self.add(self.current_screen)
        self.current_screen.show()
	