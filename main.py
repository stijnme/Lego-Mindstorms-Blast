from mindstorms import MSHub, Motor, MotorPair, ColorSensor, DistanceSensor, Appfrom
mindstorms.control import wait_for_seconds, wait_until, Timerfrom
mindstorms.operator import greater_than, greater_than_or_equal_to, less_than, less_than_or_equal_to, equal_to, not_equal_to
import math

# Create your objects here.
hub = MSHub()

# Write your program here.
hub.speaker.beep()
