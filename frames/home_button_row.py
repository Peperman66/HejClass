from gi.repository import Gtk, GdkPixbuf
from typing import Callable, List
import time

from frames import LightsFrame, WindowFrame, ProjectorFrame, GeneralFrame
from screens import OffScreen

button_filenames = ["light.png", "window.png", "projector.png", "on.png"]
other_frames = [LightsFrame, WindowFrame, ProjectorFrame, GeneralFrame]

class HomeButtonRow(Gtk.Frame):
    def __init__(self, change_other_screen: Callable, change_screen: Callable, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.on = False
        self.current_state_index = len(button_filenames)
        self.change_other_screen = change_other_screen
        self.change_screen = change_screen
        self.__add_elements()
        self.__change_button_border()

    def __change_button_border(self):
        for i in range(len(button_filenames) - 1):
            if i == self.current_state_index:
                self.box.get_children()[i].get_style_context().add_class("active")
            else:
                self.box.get_children()[i].get_style_context().remove_class("active")

    def __on_click(self, index: int):
        if index == len(button_filenames) - 1:
            self.change_screen(OffScreen)
            return
        
        if index == self.current_state_index:
            self.current_state_index = len(button_filenames) - 1
        else:
            self.current_state_index = index

        self.change_other_screen(other_frames[self.current_state_index])
        self.__change_button_border()

    def __add_elements(self):

        self.box = Gtk.Box()
        self.box.set_homogeneous(True)
        buttons: List[Gtk.Button] = [Gtk.Button() for _ in button_filenames]

        for i, name in enumerate(button_filenames):
            pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_scale(f"images/{name}", 200, 200, True)
            image = Gtk.Image.new_from_pixbuf(pixbuf)

            buttons[i].set_image(image)

        for i in range(len(buttons)):
            buttons[i].connect("clicked", lambda _, x=i: self.__on_click(x))
            self.box.pack_start(buttons[i], True, False, 20)
            buttons[i].show()
            
        self.add(self.box)
        self.props.name = "home-button-row"
        self.box.show()
        
    
