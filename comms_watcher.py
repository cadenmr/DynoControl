import serial,comms
from time import sleep

ser = serial.Serial('/dev/ttyACM0', 38400, timeout=0.2)
dyno = comms.Comms(ser)

def pretty_print(s):
    print(dyno.getTelemetry())

sleep(3)

dyno.setInletKp(0.00)
pretty_print(ser)
dyno.setInletKi(0.0001)
pretty_print(ser)
dyno.setInletIntegratorMin(-85)
pretty_print(ser)
dyno.setInletIntegratorMax(85)
pretty_print(ser)
dyno.setShaftRpmTarget(9500)
pretty_print(ser)

dyno.setOutletKp(0.00)
pretty_print(ser)
dyno.setOutletKi(0.0005)
pretty_print(ser)
dyno.setOutletIntegratorMin(-85)
pretty_print(ser)
dyno.setOutletIntegratorMax(85)
pretty_print(ser)
dyno.setOutletTargetTemperature(-200)
pretty_print(ser)

# dyno.setLoadCellResolution(128)

dyno.setLoadCellOffset(20868)
pretty_print(ser)
dyno.setLoadCellScale(-10206.808593)
pretty_print(ser)

dyno.setConfigComplete()
pretty_print(ser)

print(ser.in_waiting)
while(ser.in_waiting > 0):
    _=ser.read()

sleep(1)

while True:
    dyno.requestTelemetry()
    # sleep(0.1)
    pretty_print(ser)

    # try:
    #     pretty_print(ser)
    # except ValueError:
    #     print('ERRORED')
    #     sleep(3)