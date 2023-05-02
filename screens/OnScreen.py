from gi.repository import Gtk
from typing import Callable

from frames import HomeButtonRow, OffFrame


class OnScreen(Gtk.Frame):
    def __init__(self, change_screen: Callable, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__add_elements()
        self.__change_screen = change_screen

    def __change_other_screen(self, screen):
        self.box.remove(self.other_screen)
        self.other_screen.destroy()
        self.other_screen = screen()
        self.box.pack_start(self.other_screen, True, True, 0)
        self.other_screen.show()

    def __add_elements(self):
        self.box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.other_screen = OffFrame()
        self.box.pack_start(self.other_screen, True, True, 0)
        self.button_row = HomeButtonRow(self.__change_other_screen)
        self.box.pack_end(self.button_row, False, False, 40)

        self.other_screen.show()
        self.button_row.show()

        self.add(self.box)
        self.box.show()