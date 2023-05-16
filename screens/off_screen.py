from gi.repository import Gtk
from typing import Callable

class OffScreen(Gtk.Frame):
    def __init__(self, change_screen: Callable, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__add_elements()
        self.__change_screen = change_screen

    def __add_elements(self):
        event_box = Gtk.EventBox()
        box = Gtk.Box()
        gytool_image = Gtk.Image()
        srgh_image = Gtk.Image()
        center_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)

        event_box.add(box)

        box.pack_start(gytool_image, False, False, 0)
        box.pack_start(center_box, True, False, 0)
        box.pack_start(srgh_image, False, False, 0)

        self.time_label = Gtk.Label("TIME")
        self.date_label = Gtk.Label("DATE")
        text_label = Gtk.Label("Stiskem zapnete učebnu...")

        center_box.pack_start(self.time_label, False, False, 0)
        center_box.pack_start(self.date_label, False, False, 0)
        center_box.pack_start(text_label, False, False, 0)

        self.add(event_box)
        event_box.show()
        box.show()
        gytool_image.show()
        center_box.show()
        srgh_image.show()

        text_label.show()
        self.time_label.show()
        self.date_label.show()

        self.set_vexpand(True)
        self.set_hexpand(True)

        from screens import OnScreen
        event_box.connect("button-press-event", lambda *args: self.__change_screen(OnScreen))