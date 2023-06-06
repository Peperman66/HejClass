from gpiozero import LED, exc
from typing import Dict

class Pin(LED):
    def __init__(self, pin=None, active_high=True, initial_value=False, *args, **kwargs):
        try:
            super().__init__(pin, active_high, initial_value, *args, **kwargs)
        except exc.BadPinFactory():
            print("Probably not running on RPi!")

    def on(self):
        super().on()
        self.print_state()
    
    def off(self):
        super().off()
        self.print_state()
    
    def toggle(self):
        super().toggle()
        self.print_state()
    
    def print_state(self):
        print(f"{self.pin.number}: {self._active_state}")

    def get_state(self):
        return self.value

all_pins: Dict[str, Pin] = {
    "1": Pin("GPIO4", active_high = False, initial_value=True),
    "2": Pin("GPIO17", active_high = False, initial_value=True),
    "3": Pin("GPIO27", active_high = False, initial_value=True),
    "4": Pin("GPIO22", active_high = False, initial_value=True),
    "5": Pin("GPIO5", active_high = False, initial_value=True),
    "6": Pin("GPIO6", active_high = False, initial_value=True),
    "7": Pin("GPIO13", active_high = False, initial_value=True),
    "8": Pin("GPIO26", active_high = False, initial_value=True),
    "9": Pin("GPIO16", active_high = False, initial_value=True),
    "10": Pin("GPIO12", active_high = False, initial_value=True),
    "11": Pin("GPIO24", active_high = False, initial_value=True),
    "12": Pin("GPIO23", active_high = False, initial_value=True)
}

light_pins: Dict[str, Pin] = {
    "left": all_pins["1"],
    "middle": all_pins["2"],
    "right": all_pins["3"],
    "board": all_pins["4"]
}

window_pins: Dict[str, Pin] = {
    "left_direction": all_pins["5"],
    "left_control": all_pins["6"],
    "middle_direction": all_pins["7"],
    "middle_control": all_pins["8"],
    "right_direction": all_pins["9"],
    "right_control": all_pins["10"]
}
