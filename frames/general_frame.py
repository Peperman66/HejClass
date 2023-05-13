from gi.repository import Gtk

class GeneralFrame(Gtk.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__add_elements()

    def __add_elements(self):
        box = Gtk.Box()
        label = Gtk.Label("FUNCTIONS")
        label.show()
        self.add(label)