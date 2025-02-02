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


def get_serial():
        # readline only works when your data from the esp has \n in it
    data = se.readline()
    data = float(data) % 100
    logger.info(data)
    return data

