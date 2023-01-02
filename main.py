from mindstorms import MSHub, Motor, MotorPair, ColorSensor, DistanceSensor, App
from mindstorms.control import wait_for_seconds, wait_until, Timer
from mindstorms.operator import greater_than, greater_than_or_equal_to, less_than, less_than_or_equal_to, equal_to, not_equal_to
import math

# Functions
## Measure Distance
def measure_distance():
    dist_cm = distance_sensor.get_distance_cm()
    return dist_cm

## This calibrates Blast’s arms and head motor in port D, and runs it to the neutral position.
def calibrate():
    timer = Timer()
    timer.reset()
    motor_arms.start_at_power(100)
    wait_for_seconds(0.3)
    while motor_arms.get_speed() > 50 and timer.now() < 3:
        pass
    motor_arms.stop()
    wait_for_seconds(0.2)
    hub.motion_sensor.reset_yaw_angle()
    wait_for_seconds(0.1)
    timer.reset()
    motor_arms.start(-50)
    while hub.motion_sensor.get_yaw_angle() > -42 and timer.now() < 2:
        pass
    motor_arms.stop()
    wait_for_seconds(0.2)
    motor_arms.set_degrees_counted(0)

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

## Port B = hand
motor_hand = Motor('B')

## Port e = color sensor
color_sensor = ColorSensor('E')

## Port = distance sensor
distance_sensor = DistanceSensor('F')


# Reset arms to neutral position
calibrate()
motor_hand.run_to_position(0, 'shortest path')

# Raise arm to measure distance
motor_arms.run_for_rotations(1.8,50)

# Start driving straight forward
motor_pair.set_default_speed(-30)
motor_pair.start()
dist = measure_distance()
while dist is None:
    dist = measure_distance()

# Stop after loop
motor_pair.stop()

hub.light_matrix.write('Dist: ' + str(dist) + ' cm')
hub.speaker.start_sound('Hello',100) # Don't wait until finished
hub.light_matrix.write('Hello!')


# Return arms to starting position
motor_arms.run_for_rotations(-1.8,50)

# Time to shoot
hub.speaker.start_sound('Laser',100) # Don't wait until finished
motor_hand.run_to_degrees_counted(60,100)
hub.speaker.start_sound('Laser',100) # Don't wait until finished
motor_hand.run_to_degrees_counted(-60,100)

hub.speaker.play_sound('Target Destroyed',100)
motor_hand.run_to_degrees_counted(0,100)
