from gi.repository import Gtk

class SceneFrame(Gtk.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__add_elements()

    def __add_elements(self):
        label = Gtk.Label("SCENES")
        label.show()
        self.add(self.label)