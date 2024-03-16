from iot_device_emulation import SmartLight, Thermostat, SecurityCamera
from monitoring_dashboard import MonitoringDashboard
import random

class AutomationSystem:
    def __init__(self):
        # Initializing an empty dictionary to store all the devices
        self.devices = {}

    def add_device(self, device):
        # Adding a device to the automation system
        self.devices[device.device_id] = device

    def simulate(self):
        # Simulate the changes in each device
        for device in self.devices.values():
            # Handling SmartLight logic
            if isinstance(device, SmartLight):
                if device.status == "off":
                    device.turn_on()
                    device.brightness = random.randint(1, 100)
                elif device.status == "on":
                    device.brightness = random.randint(1, 100)
            elif isinstance(device, Thermostat):
                if device.status == "off":
                    device.set_temperature(random.randint(60, 80))
                elif device.status == "on":
                    device.set_temperature(random.randint(60, 80))
