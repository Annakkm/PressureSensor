

class BasePressureSensor:
    def __init__(self, sensor_id, location, measurement_range):

        self.sensor_id = sensor_id
        self.location = location
        self.measurement_range = measurement_range

    def display_details(self):
        pass

    def get_data(self):

        pass
