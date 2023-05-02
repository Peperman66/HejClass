from gi.repository import Gtk

class WindowFrame(Gtk.Frame):
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
        self.all_up = Gtk.Button("UP")
        self.all_stop = Gtk.Button("STOP")
        self.all_down = Gtk.Button("DOWN")

        self.all_box.pack_start(self.all_label, True, True, 10)
        self.all_box.pack_start(self.all_up, True, True, 10)
        self.all_box.pack_start(self.all_stop, True, True, 10)
        self.all_box.pack_start(self.all_down, True, True, 10)

        # Grid
        for i, text in enumerate(["PŘEDNÍ OKNO", "STŘEDNÍ OKNO", "ZADNÍ OKNO"]):
            label = Gtk.Label(text)
            self.grid.attach(label, i, 0, 1, 1)
            label.show()

        for i in range(3):
            up = Gtk.Button("UP")
            stop = Gtk.Button("STOP")
            down = Gtk.Button("DOWN")

            self.grid.attach(up, i, 1, 1, 1)
            self.grid.attach(stop, i, 2, 1, 1)
            self.grid.attach(down, i, 3, 1, 1)

            up.show()
            stop.show()
            down.show()

        self.grid.set_column_homogeneous(True)
        self.grid.set_row_homogeneous(True)
        self.grid.set_row_spacing(20)
        self.grid.set_column_spacing(20)
        self.grid.set_vexpand(True)
        self.grid.set_hexpand(True)
        # self.grid.props.margin_top = 10
        self.grid.props.margin_bottom = 10

        self.all_label.show()
        self.all_up.show()
        self.all_stop.show()
        self.all_down.show()

        self.box.show()
        self.all_box.show()
        self.grid.show()
        self.add(self.box)