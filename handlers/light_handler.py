from .pin_handler import light_pins
from typing import Union

class LightHandler():
    def __init__(self):
        pass

    def set(self, side: Union["left", "middle", "right", "board", "all"], value: bool):
        if side == "left" or side == "all":
            light_pins["left"].set_state(value)
        
        if side == "middle" or side == "all":
            light_pins["middle"].set_state(value)

        if side == "right" or side == "all":
            light_pins["right"].set_state(value)

        if side == "board" or side == "all":
            light_pins["board"].set_state(value)


light_handler = LightHandler()