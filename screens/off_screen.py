from gi.repository import Gtk
from typing import Callable
import threading
import datetime

class OffScreen(Gtk.Frame):
    def __init__(self, change_screen: Callable, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__add_elements()
        self.__change_screen = change_screen
        self.timer = None
        self.__update_datetime()

    def destroy(self, *args, **kwargs):
        self.timer.cancel()
        super().destroy(*args, **kwargs)

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

        [x.get_style_context().add_class("text-xl") for x in [self.time_label, self.date_label]]
        text_label.get_style_context().add_class("text-medium")
        text_label.get_style_context().add_class("text-italics")

        center_box.pack_start(self.time_label, False, False, 0)
        center_box.pack_start(self.date_label, False, False, 0)
        center_box.pack_start(text_label, False, False, 0)

        center_box.props.spacing = 20

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

        center_box.set_valign(Gtk.Align.CENTER)

        from screens import OnScreen
        event_box.connect("button-press-event", lambda *args: self.__change_screen(OnScreen))

    def __update_datetime(self):
        date = datetime.datetime.now()
        
        date_str = f"{date.day}. {date.month}. {date.year}"
        time = f"{str(date.hour).rjust(2, '0')}:{str(date.minute).rjust(2, '0')}:{str(date.second).rjust(2, '0')}"

        self.time_label.set_label(time)
        self.date_label.set_label(date_str)

        next_seconds = 1 - (10000 / date.microsecond)

        self.timer = threading.Timer(next_seconds, self.__update_datetime)
        self.timer.start()