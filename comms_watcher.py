import serial,dyno
from time import sleep


ser = serial.Serial('COM3', 250000, timeout=10)
dynamo = dyno.Dyno(ser)


def pretty_print(s):
    print(dynamo.getTelemetry())


sleep(3)

dynamo.setInletKp(0.00)
pretty_print(ser)
dynamo.setInletKi(0.0001)
pretty_print(ser)
dynamo.setInletIntegratorMin(-85)
pretty_print(ser)
dynamo.setInletIntegratorMax(85)
pretty_print(ser)
dynamo.setShaftRpmTarget(9500)
pretty_print(ser)

dynamo.setOutletKp(0.00)
pretty_print(ser)
dynamo.setOutletKi(0.0005)
pretty_print(ser)
dynamo.setOutletIntegratorMin(-85)
pretty_print(ser)
dynamo.setOutletIntegratorMax(85)
pretty_print(ser)
dynamo.setOutletTargetTemperature(-200)
pretty_print(ser)

# dynamo.setLoadCellResolution(128)

dynamo.setClientLoadCellOffset(-19500)
dynamo.setClientLoadCellScale(-0.00009929078014)

dynamo.setConfigComplete()
pretty_print(ser)


print(ser.in_waiting)

while(ser.in_waiting > 0):

    _=ser.read()

sleep(1)

while True:
    dynamo.requestTelemetry()
    pretty_print(ser)