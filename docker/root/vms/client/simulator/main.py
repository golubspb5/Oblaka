import os
import time
import random
import paho.mqtt.client as mqtt
from datetime import datetime

class Sensor:
    def __init__(self, name, interval):
        self.name = name
        self.interval = interval

    def generate_value(self):
        return random.uniform(0, 100)

class TemperatureSensor(Sensor):
    def generate_value(self):
        return random.uniform(20, 30) + datetime.now().year % 100

class PressureSensor(Sensor):
    def generate_value(self):
        return random.uniform(950, 1050) + datetime.now().month

class CurrentSensor(Sensor):
    def generate_value(self):
        return random.uniform(5, 20) + datetime.now().day

class VibrationSensor(Sensor):
    def generate_value(self):
        return random.uniform(0, 5)

SENSOR_CLASSES = {
    "temperature": TemperatureSensor,
    "pressure": PressureSensor,
    "current": CurrentSensor,
    "vibration": VibrationSensor
}

def main():
    sensor_type = os.getenv("SENSOR_TYPE", "temperature")
    sensor_name = os.getenv("SENSOR_NAME", "sensor_default")
    interval = int(os.getenv("INTERVAL", 5))
    broker_host = os.getenv("BROKER_HOST", "mosquitto")

    sensor_class = SENSOR_CLASSES.get(sensor_type, Sensor)
    sensor = sensor_class(sensor_name, interval)

    client = mqtt.Client()
    client.connect(broker_host, 1883, 60)

    while True:
        value = sensor.generate_value()
        payload = f'{{"name":"{sensor.name}", "value":{value:.2f}}}'
        client.publish(f"/sensor/{sensor_type}", payload)
        print(f"Published to /sensor/{sensor_type}: {payload}")
        time.sleep(sensor.interval)

if __name__ == "__main__":
    main()
