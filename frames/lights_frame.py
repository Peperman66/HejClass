from gi.repository import Gtk

class LightsFrame(Gtk.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__add_elements()


    def __add_elements(self):
        self.box = Gtk.Box()
        self.all_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.grid = Gtk.Grid()
        self.box.pack_end(self.grid, True, True, 10)
        self.box.pack_start(self.all_box, True, True, 10)

        self.all_label = Gtk.Label("VŠE")
        self.all_on = Gtk.Button("1")
        self.all_off = Gtk.Button("0")

        self.all_box.pack_start(self.all_label, True, True, 10)
        self.all_box.pack_start(self.all_on, True, True, 10)
        self.all_box.pack_start(self.all_off, True, True, 10)
        self.all_box.set_homogeneous(True)

        # Grid
        for i, text in enumerate(["LEVÁ ŘADA", "STŘEDNÍ ŘADA", "PRAVÁ ŘADA", "TABULE"]):
            label = Gtk.Label(text)
            self.grid.attach(label, i, 0, 1, 1)
            label.show()

        for i in range(4):
            full = Gtk.Button("1")
            none = Gtk.Button("0")

            if i < 3:
                half = Gtk.Button("1/2")
                self.grid.attach(half, i, 2, 1, 1)
                half.show()

            self.grid.attach(full, i, 1, 1, 1)
            self.grid.attach(none, i, 3, 1, 1)

            full.show()
            none.show()

        self.grid.set_column_homogeneous(True)
        self.grid.set_row_homogeneous(True)
        self.grid.set_row_spacing(20)
        self.grid.set_column_spacing(20)
        self.grid.set_vexpand(True)
        self.grid.set_hexpand(True)
        self.grid.props.margin_top = -5
        self.grid.props.margin_bottom = 10

        self.all_label.show()
        self.all_on.show()
        self.all_off.show()

        self.box.show()
        self.all_box.show()
        self.grid.show()
        self.add(self.box)