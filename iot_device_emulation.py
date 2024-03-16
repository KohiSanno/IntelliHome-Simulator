import random

class Device:
    def __init__(self, device_id):
        # Initialization
        self.device_id = device_id
        self.status = "off"

class SmartLight(Device):
    def __init__(self, device_id):
        # Giving initial values to smartlight 
        super().__init__(device_id)
        self.brightness = 0

    # method to turn the smart light on and off
    def turn_on(self):
        self.status = "on"
        self.brightness = random.randint(1, 100)

    def turn_off(self):
        self.status = "off"
        self.brightness = 0

class Thermostat(Device):
    def __init__(self, device_id):
        # initializing thermostat with specific attributes
        super().__init__(device_id)
        self.temperature = random.randint(60, 80)

    # method to set the temperature
    def set_temperature(self, temperature):
        self.temperature = temperature
        self.status = "on" if temperature > 60 else "off"

class SecurityCamera(Device):
    def __init__(self, device_id):
        # initializing security camera with specific attributes/initial values
        super().__init__(device_id)
        self.security_status = "disarmed"

    # methods to arm and disarm the security camera
    def arm(self):
        self.security_status = "armed"
        self.status = "on"

    def disarm(self):
        self.security_status = "disarmed"
        self.status = "off"