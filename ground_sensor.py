from base_sensor import BasePressureSensor


class GroundSensor(BasePressureSensor):
    """Class for a pressure sensor operating at ground level"""
    def __init__(self, sensor_id, location):
        """Child class constructor"""

        """ Call the parent class constructor"""
        super().__init__(sensor_id, location)
        print(f"Sensor {self.sensor_id} ground installed.")
