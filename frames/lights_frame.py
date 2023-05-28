from gi.repository import Gtk
from widgets import AspectButton

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

        box.props.margin_top = 10
        box.props.margin_bottom = 10

        all_label = Gtk.Label("VŠE")
        all_on = AspectButton(1, "1")
        all_off = AspectButton(1, "0")

        all_on.props.margin_bottom = 20
        all_off.props.margin_top = 20

        all_label.get_style_context().add_class("text-medium")
        all_on.get_style_context().add_class("text-xxl")
        all_off.get_style_context().add_class("text-xxl")

        all_box.pack_start(all_label, False, False, 0)
        all_box.pack_start(all_on, True, True, 0)
        all_box.pack_start(all_off, True, True, 0)

        all_box.props.spacing = 10

        # Grid
        for i, text in enumerate(["LEVÁ ŘADA", "STŘEDNÍ ŘADA", "PRAVÁ ŘADA", "TABULE"]):
            label = Gtk.Label(text)
            grid.attach(label, i, 0, 1, 1)
            label.get_style_context().add_class("text-medium")
            label.show()

        for i in range(4):
            full = AspectButton(1, "1")
            none = AspectButton(1, "0")

            if i < 3:
                half = AspectButton(1, "1/2")
                grid.attach(half, i, 2, 1, 1)
                half.set_vexpand(True)
                half.get_style_context().add_class("text-xl")
                half.show()

            grid.attach(full, i, 1, 1, 1)
            grid.attach(none, i, 3, 1, 1)

            full.set_vexpand(True)
            none.set_vexpand(True)

            full.get_style_context().add_class("text-xl")
            none.get_style_context().add_class("text-xl")

            full.show()
            none.show()

        grid.set_column_homogeneous(True)
        grid.set_row_homogeneous(False)
        grid.set_row_spacing(10)
        # grid.set_column_spacing(20)
        grid.set_vexpand(True)
        grid.set_hexpand(True)

        all_label.show()
        all_on.show()
        all_off.show()

        box.show()
        all_box.show()
        grid.show()
        self.add(box)