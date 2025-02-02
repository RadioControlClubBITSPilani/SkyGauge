"""
This where the serial data is being read

BEGIN WORK HERE
"""

import serial
import logging

logger = logging.getLogger("Core.Communication")


# change this to the appropriate com port on windows
se = serial.Serial('/dev/ttyUSB0')
se.baudrate = 115200


def log_serial():
    while True:

        # readline only works when your data from the esp has \n in it
        logger.info(se.readline())

