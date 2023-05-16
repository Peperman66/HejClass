from gi.repository import Gtk

class ProjectorFrame(Gtk.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__add_elements()

    def __add_elements(self):
        grid = Gtk.Grid()
        on_button = Gtk.Button("ZAP")
        off_button = Gtk.Button("VYP")
        mute_button = Gtk.Button("A/V MUTE")
        freeze_button = Gtk.Button("FREEZE")
        ports_button = Gtk.Button("PORTY")

        grid.attach(on_button, 0, 0, 1, 1)
        grid.attach(off_button, 0, 1, 1, 1)
        grid.attach(mute_button, 1, 0, 1, 1)
        grid.attach(freeze_button, 1, 1, 1, 1)
        grid.attach(ports_button, 2, 0, 1, 2)

        grid.set_row_homogeneous(True)
        grid.set_column_homogeneous(True)

        on_button.show()
        off_button.show()
        mute_button.show()
        freeze_button.show()
        ports_button.show()
        grid.show()
        self.add(grid)