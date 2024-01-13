import serial 
import serial.tools.list_ports



ARDUINO_DESCRIPTIONS = ['Arduino', 'CH340', 'USB2.0-Serial']


arduino = None
def connect():
    global arduino
    ports = list(serial.tools.list_ports.comports())

    ports = [p for p in ports if any(d in p.description for d in ARDUINO_DESCRIPTIONS)]

    if len(ports) == 0:
        print('No Arduino found')
        print('Available ports:')
        for p in list(serial.tools.list_ports.comports()):
            print(p, " - ", p.description)
        return False
    else:
        for p in ports:
            print(p)

    print('Connecting to Arduino on port: ' + ports[0].device)

    arduino = serial.Serial(ports[0].device, 9600, timeout=1)
    return True



def send(msg):
    if arduino is None or not arduino.is_open:
        print('Arduino not connected, trying to connect...')
        s = connect()
        if not s:
            print('Arduino Connection failed, message not sent')
            return
    arduino.write(msg.encode())


def read():
    if arduino is None or not arduino.is_open:
        print('Arduino not connected, trying to connect...')
        s = connect()
        if not s:
            print('Arduino Connection failed, message not sent')
            return
    return arduino.readline().decode('utf-8').strip()



send('Hello from Python')