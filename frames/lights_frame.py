from gi.repository import Gtk

class LightsFrame(Gtk.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__add_elements()


    def __add_elements(self):
        box = Gtk.Box()
        all_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        grid = Gtk.Grid()
        box.pack_end(grid, True, True, 10)
        box.pack_start(all_box, True, True, 10)

        all_label = Gtk.Label("VŠE")
        all_on = Gtk.Button("1")
        all_off = Gtk.Button("0")

        all_box.pack_start(all_label, True, True, 10)
        all_box.pack_start(all_on, True, True, 10)
        all_box.pack_start(all_off, True, True, 10)
        all_box.set_homogeneous(True)

        # Grid
        for i, text in enumerate(["LEVÁ ŘADA", "STŘEDNÍ ŘADA", "PRAVÁ ŘADA", "TABULE"]):
            label = Gtk.Label(text)
            grid.attach(label, i, 0, 1, 1)
            label.show()

        for i in range(4):
            full = Gtk.Button("1")
            none = Gtk.Button("0")

            if i < 3:
                half = Gtk.Button("1/2")
                grid.attach(half, i, 2, 1, 1)
                half.show()

            grid.attach(full, i, 1, 1, 1)
            grid.attach(none, i, 3, 1, 1)

            full.show()
            none.show()

        grid.set_column_homogeneous(True)
        grid.set_row_homogeneous(True)
        grid.set_row_spacing(20)
        grid.set_column_spacing(20)
        grid.set_vexpand(True)
        grid.set_hexpand(True)

        all_label.show()
        all_on.show()
        all_off.show()

        box.show()
        all_box.show()
        grid.show()
        self.add(box)