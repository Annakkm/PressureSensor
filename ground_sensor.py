from base_sensor import BasePressureSensor


class GroundSensor(BasePressureSensor):
    def __init__(self, sensor_id, location):
        super().__init__(sensor_id, location)
        print(f"Sensor {self.sensor_id} ground installed")
