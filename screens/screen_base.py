from gi.repository import Gtk

class ScreenBase(Gtk.Frame):
    def __init__(*args, **kwargs):
        super().__init__(*args, **kwargs)