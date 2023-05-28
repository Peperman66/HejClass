from gi.repository import Gtk

class AspectButton(Gtk.AspectFrame):
    def __init__(self, ratio, label = None, *args, **kwargs):
        super().__init__()
        super().set(0.5, 0.5, 1, False)
        self.button = Gtk.Button(label)
        self.add(self.button)
        self.button.show()
