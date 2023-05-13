from gi.repository import Gtk
from typing import Callable


class OnScreen(Gtk.Frame):
    def __init__(self, change_screen: Callable, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__change_screen = change_screen
        self.__add_elements()

    def __change_other_screen(self, screen):
        self.box.remove(self.other_screen)
        self.other_screen.destroy()
        self.other_screen = screen()
        self.box.pack_start(self.other_screen, True, True, 0)
        self.other_screen.show()

    def __add_elements(self):
        from frames import HomeButtonRow, GeneralFrame

        self.box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.other_screen = GeneralFrame()
        self.box.pack_start(self.other_screen, True, True, 0)
        button_row = HomeButtonRow(self.__change_other_screen, self.__change_screen)
        self.box.pack_end(button_row, False, False, 40)

        self.other_screen.show()
        button_row.show()

        self.add(self.box)
        self.box.show()