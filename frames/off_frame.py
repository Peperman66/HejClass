from gi.repository import Gtk

class OffFrame(Gtk.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__add_elements()

    def __add_elements(self):
        label = Gtk.Label("OFF")
        label.show()
        self.add(self.label)