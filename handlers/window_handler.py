from .pin_handler import window_pins
from typing import Union

class WindowHandler():
    def __init__(self):
        pass

    def stop(self, side: Union["front", "middle", "rear", "all"]):
        if side == "front" or side == "all":
            window_pins["front_control"].off()
        
        if side == "middle" or side == "all":
            window_pins["middle_control"].off()

        if side == "rear" or side == "all":
            window_pins["rear_control"].off()

    def run(self, side: Union["front", "middle", "rear", "all"], direction_down: bool):
        if side == "front" or side == "all":
            window_pins["front_direction"].set_state(direction_down)
            window_pins["front_control"].on()
        
        if side == "middle" or side == "all":
            window_pins["middle_direction"].set_state(direction_down)
            window_pins["middle_control"].on()

        if side == "rear" or side == "all":
            window_pins["rear_direction"].set_state(direction_down)
            window_pins["rear_control"].on()


window_handler = WindowHandler()