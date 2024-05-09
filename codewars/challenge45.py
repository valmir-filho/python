"""
The cockroach is one of the fastest insects.
Write a function which takes its speed in km per
hour and returns it in cm per second, rounded down
to the integer (= floored).
"""


def cockroach_speed(speed_km_hr):
    speed_cm_s = speed_km_hr * 100000 / 3600
    return int(speed_cm_s)
