from gi.repository import Gtk

class OnFrame(Gtk.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__add_elements()

    def __add_elements(self):
        label = Gtk.Label("ON")
        label.show()
        self.add(self.label)