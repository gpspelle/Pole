from pyb import UART, Pin, delay

UART_ID = 3 # Uses Y9 as TX and Y10 as RX

uart = UART(UART_ID, 115200)
uart.init(115200, bits=8, parity=None, stop=1)

green_button = Pin("X5", Pin.IN)
red_button = Pin("X6", Pin.IN)

count = 0

while True:

    message = None
    while message == None:
        message = uart.read()
    
    message = str(message, 'utf-8')
    print("Message from ESP32: [", message, "]")

    message = '0'
    
    #while green_button.value() + red_button.value() == 0:
    #    pass
        
    if green_button.value() == 1 and red_button.value() == 1:
        message = '3'
    elif green_button.value() == 1:
        message = '2'
    elif red_button.value() == 1:
        message = '1'

    print("Message to ESP32: [", message, "]")
    uart.write(message)

    
