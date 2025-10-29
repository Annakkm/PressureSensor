from ground_sensor import GroundSensor

import random

print("|Program for air pressure sensors for measurements at different altitudes.|")

first_sensor = GroundSensor("GS-001", "Laboratory")
first_sensor.display_details()
result_pressure = first_sensor.get_data()
print(f"Displaying results of {first_sensor.sensor_id} data pressure:{result_pressure: .2f} Pascals")