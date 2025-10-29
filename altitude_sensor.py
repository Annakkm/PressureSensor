from base_sensor import BasePressureSensor
import random


class AltitudeSensor(BasePressureSensor):
    """Class for a pressure sensor designed for altitude operations."""

    def __init__(self, sensor_id, location, max_altitude):
        """Child class constructor"""
        altitude_range = (10000, 120000)

        """ Call the parent class constructor"""
        super().__init__(sensor_id, location, measurement_range=altitude_range)
        self.max_altitude = max_altitude
        print(f"Sensor {self.sensor_id} ground installed.\n")

    def get_data(self):
        """Overridden method"""
        return 26500.0 + random.uniform(-500, 500)

    def display_details(self):
        """Overridden method"""
        super().display_details()
        print(f"Max altitude: {self.max_altitude}")
