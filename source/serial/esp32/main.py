from machine import UART

TX2 = 17
RX2 = 16

uart = UART(1, 9600)
uart.init(9600, bits=8, parity=None, stop=1, rx=RX2, tx=TX2)

while True:

    message = None
    while message == None:
        message = uart.read()

    message = str(message, 'utf-8')
    print("*****************************************")
    print("Message from PYBOARD: [", message, "]")
    uart.write("Message received sucessfully! The message is [" + message + "]")
