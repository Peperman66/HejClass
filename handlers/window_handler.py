from .pin_handler import window_pins

class WindowHandler():
    def __init__(self):
        pass

    def stop(side: "left" | "middle" | "right" | "all"):
        if side == "left" or side == "all":
            window_pins["left_control"].off()
        
        if side == "middle" or side == "all":
            window_pins["middle_control"].off()

        if side == "right" or side == "all":
            window_pins["right_control"].off()

    def run(side: "left" | "middle" | "right" | "all", direction_down: bool):
        if side == "left" or side == "all":
            window_pins["left_direction"].set_state(direction_down)
            window_pins["left_control"].on()
        
        if side == "middle" or side == "all":
            window_pins["middle_direction"].set_state(direction_down)
            window_pins["middle_control"].on()

        if side == "right" or side == "all":
            window_pins["right_direction"].set_state(direction_down)
            window_pins["right_control"].on()


window_handler = WindowHandler()