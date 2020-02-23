from machine import UART

TX2 = 17
RX2 = 16

uart = UART(1, 115200)
uart.init(115200, bits=8, parity=None, stop=1, rx=RX2, tx=TX2)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind(('', 80))
    s.listen(5)
    conn, addr = s.accept()
    with conn:
        print('Got a connection from %s' % str(addr))

        # So far ESP32 is not receiving any data
        #request = conn.recv(1024)
        while True:

            if led_r.value() == 1:
                red_button_state="ON"
            else:
                red_button_state="OFF"
            if led_g.value() == 1:
                green_button_state="ON"
            else:
                green_button_state="OFF"

            # Send to the connection the actual state
            #conn.send()

            uart.write('1')
            message = None
            while message == None:
                message = uart.read()

            message = str(message, 'utf-8')

            print("Message from PYBOARD: [", message, "]")
            if message == '3':
                led_r.value(1)
                led_g.value(1)
            elif message == '2':
                led_r.value(0)
                led_g.value(1)
            elif message == '1':
                led_r.value(1)
                led_g.value(0)
            else:
                led_r.value(0)
                led_g.value(0)
