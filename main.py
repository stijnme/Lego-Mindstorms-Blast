from mindstorms import MSHub, Motor, MotorPair, ColorSensor, DistanceSensor, Appfrom
mindstorms.control import wait_for_seconds, wait_until, Timerfrom
mindstorms.operator import greater_than, greater_than_or_equal_to, less_than, less_than_or_equal_to, equal_to, not_equal_to
import math

# Functions
## Measure Distance
def measure_distance():
    dist_cm = distance_sensor.get_distance_cm()
    return dist_cm

# TODO: create function to remember arm position

# Create your objects here.
hub = MSHub()

# Write your program here.
hub.speaker.beep()

# Initialize connected sensors
## Port a = left leg
## Port c = right leg
motor_pair = MotorPair('A','C')

motor_arms = Motor('D')

## Port e = color sensor
color_sensor = ColorSensor('E')

## Port = distance sensor
distance_sensor = DistanceSensor('F')


# Reset arms to neutral position
#motor_arms.run_to_position(0, 'shortest path')

# Set speed
motor_pair.set_default_speed(50)
# Move for 2 seconds
motor_pair.move(2, 'seconds')
# Move into the other direction
motor_pair.set_default_speed(-50)
motor_pair.move(2, 'seconds')

# Raise arm to measure distance
motor_arms.run_for_rotations(1.8,50)

dist = measure_distance()
while dist is None:
    motor_pair.move(1, 'seconds')
    dist = measure_distance()

hub.light_matrix.write(str(dist) + ' cm from target')
hub.speaker.start_sound('Hello',100) # Don't wait until finished
hub.light_matrix.write('Hello!')


# Return arms to starting position
motor_arms.run_for_rotations(-1.8,50)
