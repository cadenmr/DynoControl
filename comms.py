import struct

class Comms:

    def __init__(self, port, endian='little'):

        self.ser = port

        if (endian == 'little'):
            self.endian = True
        elif (endain == 'big'):
            self.endian = False
        else:
            raise ValueError('endian must be either "big" or "little"')

    def _packBoolean(self, val):

        sendData = b'\x00\x00\x00\x00'

        if (val):
            sendData += b'\x01'
        else:
            sendData += b'\x00'

        return sendData

    def _packByte(self, val):

        if (val > 255 or val < 0):
            raise ValueError('number out of range')

        sendData = b'\x00\x00\x00\x00'

        if (self.endian):
            sendData += struct.pack('<b', val)
        else:
            sendData += struct.pack('>b', val)

        return sendData

    def _packUnsignedInt(self, val):

        if (val > 65535 or val < 0):
            raise ValueError('number out of range')

        sendData = b'\x00\x00\x00'

        if (self.endian):
            sendData += struct.pack('<H', val)
        else:
            sendData += struct.pack('>H', val)

        return sendData
        
    def _packSignedInt(self, val):

        if (val > 32767 or val < -32768):
            raise ValueError('number out of range')

        sendData = b'\x00\x00\x00'

        if (self.endian):
            sendData += struct.pack('<h', val)
        else:
            sendData += struct.pack('>h', val)

        return sendData

    def _packUnsignedLong(self, val):

        if (val > 4294967295 or val < 0):
            raise ValueError('number out of range')

        sendData = b'\x00'
        
        if (self.endian):
            sendData += struct.pack('<L', val)
        else:
            sendData += struct.pack('>L', val)

        return sendData

    def _packDouble(self, val):

        sendData = b'\x00'
        
        if (self.endian):
            sendData += struct.pack('<f', val)
        else:
            sendData += struct.pack('>f', val)

        return sendData

    def _packNull(self):
        return b'\x00\x00\x00\x00\x00'

    # shaft rpm parameters
    def setShaftRpmMaximum(self, val):
        self.ser.write(b'\x00')
        self.ser.write(self._packUnsignedInt(val))
    
    def setShaftRpmMaximumHysteresis(self, val):
        self.er.write(b'\x01')
        self.ser.write(self._packUnsignedInt(val))

    def setShaftRpmRounding(self, val):
        self.ser.write(b'\x02')
        self.ser.write(self._packByte(val))

    def setShaftRpmTimeout(self, val):
        self.ser.write(b'\x03')
        self.ser.write(self._packUnsignedLong(val))

    def setShaftRpmTarget(self, val):
        self.ser.write(b'\x04')
        self.ser.write(self._packUnsignedInt(val))

    # inlet valve parameters
    def setInletKp(self, val):
        self.ser.write(b'\x05')
        self.ser.write(self._packDouble(val))

    def setInletKi(self, val):
        self.ser.write(b'\x06')
        self.ser.write(self._packDouble(val))

    def setInletKd(self, val):
        self.ser.write(b'\x07')
        self.ser.write(self._packDouble(val))

    def setInletIntegratorMin(self, val):
        self.ser.write(b'\x08')
        self.ser.write(self._packDouble(val))

    def setInletIntegratorMax(self, val):
        self.ser.write(b'\x09')
        self.ser.write(self._packDouble(val))

    def setInletMinimumDuty(self, val):
        self.ser.write(b'\x0a')
        self.ser.write(self._packByte(val))

    def setInletMaximumDuty(self, val):
        self.ser.write(b'\x0b')
        self.ser.write(self._packByte(val))

    def enableInletOverride(self, val):
        self.ser.write(b'\x0c')
        self.ser.write(self._packBoolean(val))

    def setInletOverrideDuty(self, val):
        self.ser.write(b'\x0d')
        self.ser.write(self._packByte(val))

    # outlet valve parameters
    def setOutletKp(self, val):
        self.ser.write(b'\x0e')
        self.ser.write(self._packDouble(val))

    def setOutletKi(self, val):
        self.ser.write(b'\x0f')
        self.ser.write(self._packDouble(val))

    def setOutletKd(self, val):
        self.ser.write(b'\x10')
        self.ser.write(self._packDouble(val))

    def setOutletIntegratorMin(self, val):
        self.ser.write(b'\x11')
        self.ser.write(self._packDouble(val))

    def setOutletIntegratorMax(self, val):
        self.ser.write(b'\x12')
        self.ser.write(self._packDouble(val))

    def setOutletMinimumDuty(self, val):
        self.ser.write(b'\x13')
        self.ser.write(self._packByte(val))

    def setOutletMaximumDuty(self, val):
        self.ser.write(b'\x14')
        self.ser.write(self._packByte(val))

    def setOutletTargetTemperature(self, val):
        self.ser.write(b'\x15')
        self.ser.write(self._packDouble(val))

    def enableOutletOverride(self, val):
        self.ser.write(b'\x16')
        self.ser.write(self._packBoolean(val))

    def setOutletOverrideDuty(self, val):
        self.ser.write(b'\x17')
        self.ser.write(self._packByte(val))

    # load cell parameters
    def setLoadCellResolution(self, val):

        if (val != 64 and val != 128):
            raise ValueError("resolution must be 64 or 128")

        self.ser.write(b'\x18')
        self.ser.write(self._packByte(val))


    def setLoadCellOffset(self, val):
        self.ser.write(b'\x19')
        self.ser.write(self._packUnsignedLong(val))

    def setLoadCellScale(self, val):
        self.ser.write(b'\x1a')
        self.ser.write(self._packDouble(val))

    # misc
    def requestTelemetry(self):
        self.ser.write(b'\x1b')
        self.ser.write(self._packNull())

    def setConfigComplete(self):
        self.ser.write(b'\x1c')
        self.ser.write(self._packNull())

    def getTelemetry(self, packet=None):

        if packet is None:
            packet = self.ser.read(21)

        if (len(packet) != 21):
            raise ValueError(f'invalid packet: expected 22 bytes, got {len(packet)} bytes')

        statusByte = packet[0]
        commandPass = (statusByte & 0b00100000) != 0
        commandFail = (statusByte & 0b01000000) != 0
        critical = (statusByte & 0b00010000) != 0
        errorCode = statusByte & 0b00001111

        # if (self.endian):
        #     rpm = struct.unpack('<f', packet[1:3])[0]
        #     measuredForce = struct.unpack('<f', packet[3:7])[0]
        #     outletTemp = struct.unpack('<f', packet[9:])[0]
        # else:
        #     rpm = struct.unpack('>f', packet[1:3])[0]
        #     measuredForce = struct.unpack('>f', packet[3:7])[0]
        #     outletTemp = struct.unpack('>f', packet[9:])[0]

        # inletDuty = packet[7]
        # outletDuty = packet[8]

        if (self.endian):
            rpm = struct.unpack('<f', packet[1:5])[0]
            measuredForce = struct.unpack('<f', packet[5:9])[0]
            inletDuty = struct.unpack('<f', packet[9:13])[0]
            outletDuty = struct.unpack('<f', packet[13:17])[0]
            outletTemp = struct.unpack('<f', packet[17:21])[0]
        else:
            rpm = struct.unpack('>f', packet[1:5])[0]
            measuredForce = struct.unpack('>f', packet[5:9])[0]
            inletDuty = struct.unpack('>f', packet[9:13])[0]
            outletDuty = struct.unpack('>f', packet[13:18])[0]
            outletTemp = struct.unpack('>f', packet[18:22])[0]
    
        return (commandPass, commandFail, critical, errorCode, int(rpm), round(measuredForce, 2), 
                int(inletDuty), int(outletDuty), round(outletTemp, 2))