from .pin_handler import light_pins
from typing import Union

class LightHandler():
    def __init__(self):
        pass

    def set(self, side: Union["left", "middle", "right", "board", "all"], value: Union["off", "half", "on"]):
        if side == "left" or side == "all":
            light_pins["left_full"].set_state(value == "on")
            light_pins["left_half"].set_state(value != "off")
        
        if side == "middle" or side == "all":
            light_pins["middle_full"].set_state(value == "on")
            light_pins["middle_half"].set_state(value != "off")

        if side == "right" or side == "all":
            light_pins["right_full"].set_state(value == "on")
            light_pins["right_half"].set_state(value != "off")

        if side == "board" or side == "all":
            light_pins["board"].set_state(value != "off")


light_handler = LightHandler()