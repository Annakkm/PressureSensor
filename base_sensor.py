import random


class BasePressureSensor:
    """Parent class for an air pressure sensor."""

    def __init__(self, sensor_id, location, measurement_range: tuple = (80000, 120000)):
        """Parent class constructor"""
        self.sensor_id = sensor_id
        self.location = location
        self.measurement_range = measurement_range

    def display_details(self):
        """Method of displaying information"""
        print("Showing the results from the base class")
        print(f"ID sensor: {self.sensor_id}")
        print(f"Location: {self.location}")
        print(f"Measurement range : {self.measurement_range[0]} - {self.measurement_range[1]}")

    def get_data(self):
        """Method of obtaining a value in pascals"""
        return 101325.0 + random.uniform(-1000, 1000)

