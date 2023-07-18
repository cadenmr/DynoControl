if __name__ != "__main__":
    raise RuntimeError('program must be called directly')

import tkinter as tk
import serial
import comms

from time import sleep

serialPort = '/dev/ttyACM0'
serialRate = 115200

dynoPort = serial.Serial(serialPort, serialRate, timeout=1)
dyno = comms.Comms(dynoPort, endian='little')

sleep(5)

needNewRequest = True

while (True):

    if (needNewRequest):
        dyno.telemetryRequest()
        needNewRequest = False

    if (dynoPort.in_waiting >= 8):
        print(dyno.getTelemetry())
        needNewRequest = True