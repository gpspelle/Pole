from pyb import UART, Pin, delay

UART_ID = 3 # Uses Y9 as TX and Y10 as RX

uart = UART(UART_ID, 9600)
uart.init(9600, bits=8, parity=None, stop=1)

standard = 'Hello '

pin = Pin("X5", Pin.IN)

count = 0
#delay(1000)
while pin.value() != 1:
    count = 0

for i in range(7):

    message = standard + str(i)
    uart.write(message)

    rec_message = None
    while rec_message == None:
        rec_message = uart.read()

    print("Message from ESP32: [", rec_message, "]")
