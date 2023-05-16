from gi.repository import Gtk

class WindowFrame(Gtk.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__add_elements()


    def __add_elements(self):
        box = Gtk.Box()
        all_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        grid = Gtk.Grid()
        box.pack_end(grid, True, True, 10)
        box.pack_start(all_box, True, True, 10)

        # box.get_style_context().add_class("borders")

        all_label = Gtk.Label("VŠE")
        all_up = Gtk.Button("UP")
        all_stop = Gtk.Button("STOP")
        all_down = Gtk.Button("DOWN")

        all_box.pack_start(all_label, True, True, 0)
        all_box.pack_start(all_up, True, True, 0)
        all_box.pack_start(all_stop, True, True, 0)
        all_box.pack_start(all_down, True, True, 0)

        all_box.props.spacing = 20
        all_box.props.homogeneous = True

        # Grid
        for i, text in enumerate(["PŘEDNÍ OKNO", "STŘEDNÍ OKNO", "ZADNÍ OKNO"]):
            label = Gtk.Label(text)
            grid.attach(label, i, 0, 1, 1)
            label.show()

        for i in range(3):
            up = Gtk.Button("UP")
            stop = Gtk.Button("STOP")
            down = Gtk.Button("DOWN")

            grid.attach(up, i, 1, 1, 1)
            grid.attach(stop, i, 2, 1, 1)
            grid.attach(down, i, 3, 1, 1)

            up.show()
            stop.show()
            down.show()

        grid.set_column_homogeneous(True)
        grid.set_row_homogeneous(True)
        grid.set_row_spacing(20)
        grid.set_column_spacing(20)
        grid.set_vexpand(True)
        grid.set_hexpand(True)
        # grid.get_style_context().add_class("window_grid")
        # grid.props.margin_top = 10
        # grid.props.margin_bottom = 10

        all_label.show()
        all_up.show()
        all_stop.show()
        all_down.show()

        box.show()
        all_box.show()
        grid.show()
        self.add(box)