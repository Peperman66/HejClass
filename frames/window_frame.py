from gi.repository import Gtk
from widgets import AspectButton
from handlers import window_handler

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
        box.props.margin_top = 10
        box.props.margin_bottom = 10

        # box.get_style_context().add_class("borders")

        all_label = Gtk.Label("VŠE")
        all_up = AspectButton(1, "UP")
        all_stop = AspectButton(1, "STOP")
        all_down = AspectButton(1, "DOWN")

        all_up.button.connect("clicked", lambda _: window_handler.run("all", False))
        all_stop.button.connect("clicked", lambda _: window_handler.stop("all"))
        all_down.button.connect("clicked", lambda _: window_handler.run("all", True))

        all_box.pack_start(all_label, False, False, 0)
        all_box.pack_start(all_up, True, True, 0)
        all_box.pack_start(all_stop, True, True, 0)
        all_box.pack_start(all_down, True, True, 0)

        all_label.get_style_context().add_class("text-medium")
        all_up.get_style_context().add_class("text-medium")
        all_stop.get_style_context().add_class("text-medium")
        all_down.get_style_context().add_class("text-medium")

        all_buttons = [all_up, all_stop, all_down]
        for button in all_buttons:
            button.set_vexpand(True)

        all_label.set_halign(Gtk.Align.CENTER)
        all_label.set_valign(Gtk.Align.CENTER)

        all_box.props.spacing = 10
        all_box.props.homogeneous = False

        # Grid
        for i, text in enumerate(["PŘEDNÍ OKNO", "STŘEDNÍ OKNO", "ZADNÍ OKNO"]):
            label = Gtk.Label(text)
            grid.attach(label, i, 0, 1, 1)
            label.set_halign(Gtk.Align.CENTER)
            label.set_valign(Gtk.Align.CENTER)
            label.get_style_context().add_class("text-medium")
            label.show()

        row_names = ["front", "middle", "rear"]
        for i in range(3):
            up = AspectButton(1, "UP")
            stop = AspectButton(1, "STOP")
            down = AspectButton(1, "DOWN")

            up.button.connect("clicked", lambda _, x=i: window_handler.run(row_names[x], False))
            stop.button.connect("clicked", lambda _, x=i: window_handler.stop(row_names[x]))
            down.button.connect("clicked", lambda _, x=i: window_handler.run(row_names[x], True))

            up.set_vexpand(True)
            stop.set_vexpand(True)
            down.set_vexpand(True)

            up.get_style_context().add_class("text-medium")
            stop.get_style_context().add_class("text-medium")
            down.get_style_context().add_class("text-medium")

            grid.attach(up, i, 1, 1, 1)
            grid.attach(stop, i, 2, 1, 1)
            grid.attach(down, i, 3, 1, 1)

            up.show()
            stop.show()
            down.show()

        grid.set_column_homogeneous(True)
        grid.set_row_homogeneous(False)
        grid.set_row_spacing(10)
        # grid.set_column_spacing(20)
        # grid.set_vexpand(True)
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