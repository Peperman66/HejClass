from .pin_handler import light_pins

class LightHandler():
    def __init__(self):
        pass

    def on(side: "left" | "middle" | "right" | "board" | "all"):
        if side == "left" or side == "all":
            light_pins["left"].on()
        
        if side == "middle" or side == "all":
            light_pins["middle"].on()

        if side == "right" or side == "all":
            light_pins["right"].on()

        if side == "board" or side == "all":
            light_pins["board"].on()

    def off(side: "left" | "middle" | "right" | "board" | "all"):
        if side == "left" or side == "all":
            light_pins["left"].off()
        
        if side == "middle" or side == "all":
            light_pins["middle"].off()

        if side == "right" or side == "all":
            light_pins["right"].off()

        if side == "board" or side == "all":
            light_pins["board"].off()


light_handler = LightHandler()