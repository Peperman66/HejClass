from gi.repository import Gtk
from typing import Callable, List
import time

from frames import FunctionFrame, LightsFrame, WindowFrame, ProjectorFrame, SceneFrame, OnFrame, OffFrame

button_names = ["Zap/Vyp", "Akce", "Světla", "Okna", "Projektor", "Scény"]
other_frames = [FunctionFrame, LightsFrame, WindowFrame, ProjectorFrame, SceneFrame]

class HomeButtonRow(Gtk.Frame):
    def __init__(self, change_other_screen: Callable, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.on = False
        self.current_state_index = -1
        self.change_other_screen = change_other_screen
        self.__add_elements()
        self.__change_button_visibility()
        self.__turn_off()

    def __turn_off(self):
        self.on = False
        self.box.get_children()[0].set_label("Vyp")

    def __turn_on(self):
        self.on = True
        self.box.get_children()[0].set_label("Zap")

    def __change_button_visibility(self):
        for i in range(1, len(button_names)):
            if i == self.current_state_index or (self.current_state_index == -1 and i > 0):
                self.box.get_children()[i].set_sensitive(False)
            else:
                self.box.get_children()[i].set_sensitive(True)

    def __on_click(self, index: int):
        if index == 0:
            if self.on:
                self.current_state_index = -1
                self.__turn_off()
                self.change_other_screen(OffFrame)
            else:
                self.current_state_index = 0
                self.__turn_on()
                self.change_other_screen(OnFrame)
        else:
            self.current_state_index = index
            self.change_other_screen(other_frames[index-1])
        self.__change_button_visibility()

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
        
    
