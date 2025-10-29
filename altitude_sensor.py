from base_sensor import BasePressureSensor
import random


class AltitudeSensor(BasePressureSensor):
    def __init__(self, sensor_id, location, max_altitude):
        altitude_range = (10000, 120000)
        super().__init__(sensor_id, location, measurement_range=altitude_range)
        self.max_altitude = max_altitude
        print(f"Sensor {self.sensor_id} ground installed.\n")

    def get_data(self):
        return 26500.0 + random.uniform(-500, 500)

    def display_details(self):
        super().display_details()
        print(f"Max altitude: {self.max_altitude}")
