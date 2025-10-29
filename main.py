from ground_sensor import GroundSensor
from altitude_sensor import AltitudeSensor

print("|Program for air pressure sensors for measurements at different altitudes.|\n")

ground_sensor = GroundSensor("GS-001", "Laboratory")
altitude_sensor = AltitudeSensor("AL-003", "Aircraft", 12000.0)

sensors_list = [ground_sensor, altitude_sensor]

for sensor in sensors_list:
    sensor.display_details()
    print(f"Displaying results of {sensor.sensor_id} data pressure:{sensor.get_data(): .2f} Pascals")
    print("-" * 65)

