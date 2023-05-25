from gi.repository import Gtk
from typing import Callable


class OnScreen(Gtk.Frame):
    def __init__(self, change_screen: Callable, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__change_screen = change_screen
        self.other_screen = None
        self.__add_elements()

    def __change_other_screen(self, screen):
        if self.other_screen:
            self.box.remove(self.other_screen)
            self.other_screen.destroy()
        self.other_screen = screen()
        self.box.pack_start(self.other_screen, True, True, 0)

        self.other_screen.get_style_context().add_class('upper-frame')

        self.other_screen.show()

    def __add_elements(self):
        from frames import HomeButtonRow, GeneralFrame

        self.get_style_context().add_class("borders")

        self.box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.box.props.name = "on-box"
        button_row = HomeButtonRow(self.__change_other_screen, self.__change_screen)
        self.box.pack_end(button_row, False, False, 0)

        button_row.show()

        self.__change_other_screen(GeneralFrame)

        self.add(self.box)
        self.box.show()