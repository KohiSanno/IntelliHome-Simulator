
from iot_device_emulation import SmartLight, Thermostat, SecurityCamera
from monitoring_dashboard import MonitoringDashboard
from automation_system import AutomationSystem
import tkinter as tk

def main():
    # Initialize the iot devices
    light = SmartLight("Light 1")
    thermostat = Thermostat("Thermostat 1")
    security_camera = SecurityCamera("Security Camera 1")

    # Add the devices to the automation system
    automation_system = AutomationSystem()
    automation_system.add_device(light)
    automation_system.add_device(thermostat)
    automation_system.add_device(security_camera)

    # Create a dashboard for monitoring and controlling the devices
    dashboard = MonitoringDashboard(automation_system)

    # A function to update the dashboard periodically
    def update_dashboard():
        for i in range(10):
            automation_system.simulate()
            dashboard.dashboard.after(1000, update_dashboard)

    # Start the dashboard update 
    update_dashboard()

    # the script only runs if its the main program
    if __name__ == "__main__":
        main()




