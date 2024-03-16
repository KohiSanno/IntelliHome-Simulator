"""
# monitoring_dashboard.py
import tkinter as tk
from tkinter import ttk
from iot_device_emulation import SmartLight, Thermostat, SecurityCamera
import random


# monitoring_dashboard.py (Updated)
class MonitoringDashboard:
    def __init__(self, automation_system):
        self.automation_system = automation_system
        self.dashboard = tk.Tk()
        self.dashboard.title("Smart Home Monitoring Dashboard")

        self.create_widgets()
        self.dashboard.mainloop()

    def create_widgets(self):
         for device in self.automation_system.devices.values():
            frame = tk.Frame(self.dashboard, relief="solid", borderwidth=1)
            frame.configure(bg='white')
            frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S), padx=10, pady=10)

            ttk.Label(frame, text=f"{device.device_id} - {type(device).__name__} Status: {device.status}").grid(row=0, column=0)

            if isinstance(device, SmartLight):
                brightness_scale = ttk.Scale(frame, from_=0, to=100, orient=tk.HORIZONTAL)
                brightness_scale.set(device.brightness)
                brightness_scale.grid(row=1, column=0)

                def on_brightness_change(value):
                    device.brightness = value
                    status_label.config(text=f"{device.device_id} - {device.brightness}%")

                brightness_scale.config(command=on_brightness_change)
                toggle_button = ttk.Button(frame, text="Toggle ON/OFF", command=lambda: toggle(device, status_label))
                toggle_button.grid(row=2, column=0)
                status_label = ttk.Label(frame, text=f"{device.device_id} - {device.brightness}%")
                status_label.grid(row=3, column=0)

            elif isinstance(device, Thermostat):
                temperature_scale = ttk.Scale(frame, from_=60, to=80, orient=tk.HORIZONTAL)
                temperature_scale.set(device.temperature)
                temperature_scale.grid(row=1, column=0)

                def on_temperature_change(value):
                    device.set_temperature(value)
                    status_label.config(text=f"{device.device_id} - {device.temperature}C")

                temperature_scale.config(command=on_temperature_change)
                toggle_button = ttk.Button(frame, text="Toggle ON/OFF", command=lambda: toggle(device, status_label))
                toggle_button.grid(row=2, column=0)
                status_label = ttk.Label(frame, text=f"{device.device_id} - {device.temperature}C")
                status_label.grid(row=3, column=0)


            elif isinstance(device, Thermostat):
                temperature_scale = ttk.Scale(frame, from_=60, to=80, orient=tk.HORIZONTAL)
                temperature_scale.set(device.temperature)
                temperature_scale.grid(row=1, column=0)

                def on_temperature_change(value):
                    device.set_temperature(value)
                    status_label.config(text=f"{device.device_id} - {device.temperature}C")

                temperature_scale.config(command=on_temperature_change)
                toggle_button = ttk.Button(frame, text="Toggle ON/OFF", command=lambda: toggle(device, status_label))
                toggle_button.grid(row=2, column=0)
                status_label = ttk.Label(frame, text=f"{device.device_id} - {device.temperature}C")
                status_label.grid(row=3, column=0)

            elif isinstance(device, SecurityCamera):
                def toggle(device, status_label):
                    if device.status == "on":
                        device.disarm()
                    else:
                        device.arm()
                    status_label.config(text=f"{device.device_id} - Motion: {'YES' if device.status == 'on' else 'NO'}")

                toggle_button = ttk.Button(frame, text="Toggle ON/OFF", command=lambda: toggle(device, status_label))
                toggle_button.grid(row=2, column=0)
                status_label = ttk.Label(frame, text=f"{device.device_id} - Motion: {'YES' if device.status == 'on' else 'NO'}")
                status_label.grid(row=3, column=0)
"""



import random
import threading
import tkinter as tk
from tkinter import ttk
from iot_device_emulation import SmartLight, Thermostat, SecurityCamera

# Flags for tracking the state of each device and thread
light_flg = False
temp_flg = False
motion_flg = False

light_thread_flg = False
temp_thread_flg = False
motion_thread_flg = False

class MonitoringDashboard:
    def __init__(self):
        # initializing IoT devices
        self.devices = [
            SmartLight("Living Room Light"),
            Thermostat("Living Room Thermostat"),
            SecurityCamera("Front Door Camera")
        ]

        # setting up the main Tkinter window
        self.dashboard = tk.Tk()
        self.dashboard.title("IoT Device Simulator")
        self.create_widgets()

    def create_widgets(self):
        # Creating main and secondary frames for the dashboard
        frame = tk.Frame(self.dashboard, relief="solid", borderwidth=1, pady=50)
        frame.configure(bg='white')
        frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        frame_secondary = tk.Frame(self.dashboard, relief="solid")
        frame_secondary.pack(fill=tk.BOTH, expand=True, padx=50, pady=10)
        style = ttk.Style(self.dashboard)
        style.configure('Horizontal.TScale', highlightbackground="red")
        
        #primary labels
        primary_light_lbl = ttk.Label(frame, text="")
        primary_temp_lbl = ttk.Label(frame, text="")
        primary_motion_lbl = ttk.Label(frame, text="")

        #secondary labels
        device_brightness_label = ttk.Label(frame_secondary, text="")
        device_brightness_status_label = ttk.Label(frame_secondary, text="Living Room Light - 0%")

        temp_status_label_text = f"Living Room Thermostat Temperature - 0C"
        temp_status_label = ttk.Label(frame_secondary, text=temp_status_label_text)

        security_status_label_text = f"Front Door Camera - Motion: NO"
        security_status_label = ttk.Label(frame_secondary, text=security_status_label_text)
        
        # Define functions to simulate random changes in device status 
        def random_lights(label):
            label.config(text=f"Living Room Light - {random.randint(0, 100) }%")
            self.dashboard.after(1000, random_lights, label)

        def random_temp(label):
            label.config(text=f"Living Room Thermostat Temperature - {random.randint(60, 80) }C")
            self.dashboard.after(1000, random_temp, label)

        def random_motion(label, device):
            val = random.randint(0,1)
            # if val == 1:
            #     device.brightness = 100
            #     device_brightness_label.config(text=device.brightness)
            #     primary_light_lbl.config(text=f"Living Room Light: SmartLight Status: on")
            label.config(text=f"Front Door Camera - Motion: {'YES' if val == 1 else 'NO'}")
            self.dashboard.after(1000, random_motion, label, device)

        # Create threads for asynchronous device status updates
        thread = threading.Thread(target=random_lights, args=(device_brightness_status_label,))
        temp_thread = threading.Thread(target=random_temp, args=(temp_status_label,))
        motion_thread = threading.Thread(target=random_motion, args=(security_status_label, self.devices[0],))

        # go over each device and create UI components for each
        for device in self.devices:
            brightness_scale = ttk.Scale(frame_secondary, from_=0, to=100, command=lambda value=device, dev=device, label=device_brightness_label, sts_label=device_brightness_status_label:adjust_lights(value, dev, label, sts_label), orient=tk.HORIZONTAL)
            # label_text = f"{device.device_id} - {type(device).__name__} Status: {device.status}"
            # ttk.Label(frame, text=label_text).pack()

            if isinstance(device, SmartLight):
                # Label on big box
                label_text = f"Living Room Light: {type(device).__name__} Status: {device.status}"
                primary_light_lbl.config(text=label_text)
                primary_light_lbl.pack()

                # Components on secondary frame
                

                def toggle_lights():
                    global light_flg
                    global light_thread_flg
                    flag = light_flg
                    if not flag:
                        primary_light_lbl.config(text=f"Living Room Light: SmartLight Status: on")
                        light_flg = True
                        if not light_thread_flg:
                            thread.start()
                            light_thread_flg = True
                    else:
                        primary_light_lbl.config(text=f"Living Room Light: SmartLight Status: off")
                        light_flg = False
                        thread.join()
                     

                def adjust_lights(value,dev,label, sts_label):
                    tmp_brightness = int(float(value))
                    dev.brightness = tmp_brightness
                    label.config(text=f"{tmp_brightness}")
                    

                ttk.Label(frame_secondary, text="Living Room Light Brightness").pack()
                status_label_text = f"{device.device_id} - {device.brightness}%"
                device_brightness_label.pack()
                
                brightness_scale.set(device.brightness)
                brightness_scale.pack()

                toggle_button = ttk.Button(frame_secondary, text="Toggle ON/OFF", command=toggle_lights)
                toggle_button.pack()

                
                device_brightness_status_label.pack()

            elif isinstance(device, Thermostat):
                # Label on big box
                label_text = f"Living Room Thermostat: {type(device).__name__} Status: {device.status}"
                primary_temp_lbl.config(text=label_text)
                primary_temp_lbl.pack()
                # Components on secondary frame
                def toggle_temps():
                    global temp_flg
                    global temp_thread_flg
                    flag = temp_flg
                    
                    if not flag:
                        primary_temp_lbl.config(text=f"Living Room Thermostat: Thermostat Status: on")
                        temp_flg = True
                        if not temp_thread_flg:
                            temp_thread.start()
                            temp_thread_flg = True
                    else:
                        primary_temp_lbl.config(text=f"Living Room Thermostat: Thermostat Status: off")
                        temp_flg = False
                    

                def adjust_temps(value,dev,label, sts_label):
                    tmp_temperature = int(float(value))
                    dev.brightness = tmp_temperature
                    label.config(text=f"{tmp_temperature}")

                    sts_label.config(text=f"{dev.device_id} Temperature - {dev.temperature}C")

                ttk.Label(frame_secondary, text="Living Room Thermostat Temperature").pack()
                temp_label = ttk.Label(frame_secondary, text=device.temperature)
                

                temp_label.pack()
                temperature_scale = ttk.Scale(frame_secondary, from_=60, to=80, variable=device.temperature, command=lambda value=device, dev=device, label=temp_label, sts_label=temp_status_label:adjust_temps(value, dev,label, sts_label), orient=tk.HORIZONTAL)
                temperature_scale.set(device.temperature)
                temperature_scale.pack()

                toggle_button = ttk.Button(frame_secondary, text="Toggle ON/OFF", command=toggle_temps)
                toggle_button.pack()
                temp_status_label.pack()

            elif isinstance(device, SecurityCamera):

                # Label on big box
                label_text = f"Front Door Camera: {type(device).__name__} Status: {device.status}"
                primary_motion_lbl.config(text=label_text)
                primary_motion_lbl.pack()

                # Components on secondary frame
                ttk.Label(frame_secondary, text="Front Door Camera Motion Detection").pack()
                def toggle_status():
                    global motion_flg
                    global motion_thread_flg
                    flag = motion_flg
                    if not flag:
                        primary_motion_lbl.config(text=f"Front Door Camera: SecurityCamera Status: on")
                        motion_flg = True
                        if not motion_thread_flg:
                            motion_thread.start()
                            motion_thread_flg = True
                    else:
                        primary_motion_lbl.config(text=f"Front Door Camera: SecurityCamera Status: off")
                        motion_flg = False
                        motion_thread.join()

                def random_detect(dev, label, scale):
                    k = random.randint(0, 1) 
                    if k == 1:
                        dev.arm()
                        dev.brightness = 100
                        scale.set(100)
                    else:
                        dev.disarm()

                    label_text = f"{dev.device_id} - Motion: {'YES' if dev.status == 'on' else 'NO'}"
                    label.config(text=label_text)
                    primary_motion_lbl.config(text=f"Front Door Camera: {type(device).__name__} Status: {'on' if dev.status == 'on' else 'off'}")

                random_button = ttk.Button(frame_secondary, text="Random Detect Motion", command=lambda dev=device, label=security_status_label, scale=brightness_scale: random_detect(dev, label, scale))
                random_button.pack()

                toggle_button = ttk.Button(frame_secondary, text="Toggle ON/OFF", command=toggle_status)
                toggle_button.pack()

                security_status_label.pack()
                ttk.Label(frame_secondary, text="Automation Rule: Turn on lights when motion is detected").pack()

    # starting the main event loop
    def display(self):
        self.dashboard.mainloop()

# initialize and display dashboard
dashboard = MonitoringDashboard()
dashboard.display()
    


