from gi.repository import Gtk
from typing import Callable, List
import time

from frames import LightsFrame, WindowFrame, ProjectorFrame, GeneralFrame
from screens import OffScreen

button_names = ["Světla", "Okna", "Projektor", "Vyp"]
other_frames = [LightsFrame, WindowFrame, ProjectorFrame, GeneralFrame]

class HomeButtonRow(Gtk.Frame):
    def __init__(self, change_other_screen: Callable, change_screen: Callable, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.on = False
        self.current_state_index = len(button_names)
        self.change_other_screen = change_other_screen
        self.change_screen = change_screen
        self.__add_elements()
        self.__change_button_border()

    def __change_button_border(self):
        for i in range(len(button_names) - 1):
            if i == self.current_state_index:
                self.box.get_children()[i].get_style_context().add_class("active")
            else:
                self.box.get_children()[i].get_style_context().remove_class("active")

    def __on_click(self, index: int):
        if index == len(button_names) - 1:
            self.change_screen(OffScreen)
            return
        
        if index == self.current_state_index:
            self.current_state_index = len(button_names) - 1
        else:
            self.current_state_index = index

        self.change_other_screen(other_frames[self.current_state_index])
        self.__change_button_border()

    def __add_elements(self):
        self.box = Gtk.Box()
        self.box.set_homogeneous(True)
        buttons: List[Gtk.Button] = [Gtk.Button(name) for name in button_names]
        for i in range(len(buttons)):
            buttons[i].connect("clicked", lambda _, x=i: self.__on_click(x))
            self.box.pack_start(buttons[i], True, True, 20)
            buttons[i].set_hexpand(True)
            buttons[i].show()
            
        self.add(self.box)
        self.box.show()
        
    
