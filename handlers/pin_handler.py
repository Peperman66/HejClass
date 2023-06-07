from gpiozero import LED, exc
from typing import Dict

class Pin(LED):
    def __init__(self, pin=None, active_high=True, initial_value=False, *args, **kwargs):
        super().__init__(pin, active_high, initial_value, *args, **kwargs)

    def on(self):
        super().on()
        self.print_state()
    
    def off(self):
        super().off()
        self.print_state()

    def set_state(self, state):
        if state is True:
            self.on()
        else:
            self.off()
    
    def toggle(self):
        super().toggle()
        self.print_state()
    
    def print_state(self):
        print(f"{self.pin.number}: {self.is_active}")

    def get_state(self):
        return self.value

all_pins: Dict[str, Pin] = {
    "1": Pin("GPIO2", active_high = False, initial_value=False),
    "2": Pin("GPIO3", active_high = False, initial_value=False),
    "3": Pin("GPIO4", active_high = False, initial_value=False),
    "4": Pin("GPIO17", active_high = False, initial_value=False),
    "5": Pin("GPIO27", active_high = False, initial_value=False),
    "6": Pin("GPIO22", active_high = False, initial_value=False),
    "7": Pin("GPIO23", active_high = False, initial_value=False),
    "8": Pin("GPIO24", active_high = False, initial_value=False),
    "9": Pin("GPIO10", active_high = False, initial_value=False),
    "10": Pin("GPIO9", active_high = False, initial_value=False),
    "11": Pin("GPIO25", active_high = False, initial_value=False),
    "12": Pin("GPIO11", active_high = False, initial_value=False),
    "13": Pin("GPIO8", active_high = False, initial_value=False),
    "14": Pin("GPIO7", active_high = False, initial_value=False),
    "15": Pin("GPIO1", active_high = False, initial_value=False),
    "16": Pin("GPIO0", active_high = False, initial_value=False),
}

light_pins: Dict[str, Pin] = {
    "left_full": all_pins["1"],
    "left_half": all_pins["2"],
    "middle_full": all_pins["3"],
    "middle_half": all_pins["4"],
    "right_full": all_pins["5"],
    "right_half": all_pins["6"],
    "board": all_pins["7"]
}

window_pins: Dict[str, Pin] = {
    "front_direction": all_pins["8"],
    "middle_direction": all_pins["9"],
    "rear_direction": all_pins["10"],
    "all_control": all_pins["11"]
}
