from .pin_handler import window_pins
from typing import Union

class WindowHandler():
    def __init__(self):
        pass

    def stop(self):
        window_pins["all_control"].off()

    def run(self, side: Union["front", "middle", "rear", "all"], direction_down: bool):
        if side == "front" or side == "all":
            window_pins["front_direction"].set_state(direction_down)
        
        if side == "middle" or side == "all":
            window_pins["middle_direction"].set_state(direction_down)

        if side == "rear" or side == "all":
            window_pins["rear_direction"].set_state(direction_down)

        window_pins["all_control"].on()


window_handler = WindowHandler()