#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile


# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Create your objects here.

#Initialize
ev3 = EV3Brick()

#possable colors inputs
POSSIBLE_COLORS = (Color.RED, Color.GREEN, Color.BLUE, Color.YELLOW, Color.WHITE)

#Initialize motor
base_motor = Motor(Port.A, Direction.COUNTERCLOCKWISE, [8, 40])
second_motor = Motor(Port.B, Direction.COUNTERCLOCKWISE, [8, 40])

#Initialize sensor
base_switch = ColorSensor(Port.S1)

# Write your program here.

#Main loop
while True:
    color_list = []

    while len(color_list) < 8:
        base_motor.run(-100)