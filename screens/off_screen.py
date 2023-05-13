from gi.repository import Gtk
from typing import Callable

class OffScreen(Gtk.Frame):
    def __init__(self, change_screen: Callable, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__add_elements()
        self.__change_screen = change_screen

    def __add_elements(self):
        on_button = Gtk.Button("Zapnout")
        
        from screens import OnScreen
        on_button.connect("clicked", lambda x: self.__change_screen(OnScreen))

        self.add(on_button)
        on_button.show()