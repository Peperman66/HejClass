from gi.repository import Gtk
from widgets import AspectButton

class GeneralFrame(Gtk.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__add_elements()

    def __add_elements(self):
        box = Gtk.Box()

        box.props.margin_top = 10
        box.props.margin_bottom = 10

        box.set_homogeneous(True)

        # LIGHTS
        light_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        light_box.props.spacing = 40
        light_on = AspectButton(1, "ZAP")
        light_off = AspectButton(1, "VYP")

        light_on.get_style_context().add_class("text-xxl")
        light_off.get_style_context().add_class("text-xxl")

        light_box.pack_start(light_on, True, True, 0)
        light_box.pack_end(light_off, True, True, 0)
        box.pack_start(light_box, True, True, 0)

        light_on.show()
        light_off.show()
        light_box.show()


        # WINDOWS
        window_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        window_box.props.spacing = 10

        window_up = AspectButton(1, "UP")
        window_stop = AspectButton(1, "STOP")
        window_down = AspectButton(1, "DOWN")

        window_up.get_style_context().add_class("text-large")
        window_stop.get_style_context().add_class("text-large")
        window_down.get_style_context().add_class("text-large")

        window_box.pack_start(window_up, True, True, 0)
        window_box.pack_start(window_stop, True, True, 0)
        window_box.pack_start(window_down, True, True, 0)

        window_up.show()
        window_stop.show()
        window_down.show()
        window_box.show()

        box.pack_start(window_box, True, True, 0)


        # PROJECTOR
        projector_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        projector_box.props.spacing = 40
        projector_on = AspectButton(1, "ZAP")
        projector_off = AspectButton(1, "VYP")

        projector_on.get_style_context().add_class("text-xxl")
        projector_off.get_style_context().add_class("text-xxl")

        projector_box.pack_start(projector_on, True, True, 0)
        projector_box.pack_end(projector_off, True, True, 0)
        box.pack_start(projector_box, True, True, 0)

        projector_on.show()
        projector_off.show()
        projector_box.show()


        # EMPTY SPACE
        _empty = Gtk.Box()
        box.pack_start(_empty, True, True, 0)
        _empty.set_hexpand(True)
        _empty.set_vexpand(True)
        _empty.show()



        box.show()
        self.add(box)