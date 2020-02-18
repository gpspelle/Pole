from machine import UART

def web_page():
    if led_r.value() == 1:
        red_button_state="ON"
    else:
        red_button_state="OFF"
    if led_g.value() == 1:
        green_button_state="ON"
    else:
        green_button_state="OFF"
  
    '''html = """<html><head> <title>ESP Web Server</title> <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="icon" href="data:,"> <style>html{font-family: Helvetica; display:inline-block; margin: 0px auto; text-align: center;}
    h1{color: #0F3376; padding: 2vh;}p{font-size: 1.5rem;}.button{display: inline-block; background-color: #e7bd3b; border: none; 
    border-radius: 4px; color: white; padding: 16px 40px; text-decoration: none; font-size: 30px; margin: 2px; cursor: pointer;}
    .button2{background-color: #4286f4;}</style></head><body> <h1>ESP Web Server</h1> 
    <p>GPIO state: <strong>""" + gpio_state + """</strong></p><p><a href="/?led=on"><button class="button">ON</button></a></p>
    <p><a href="/?led=off"><button class="button button2">OFF</button></a></p></body></html>"""
    '''

    html = """<html>
	    <head> 
		<title>Lelinho debugger - v0</title> 
		<meta name="viewport" content="width=device-width, initial-scale=1">
    		<link rel="icon" href="data:,"> 
		<style>html{font-family: Helvetica; display:inline-block; margin: 0px auto; text-align: center;}
    h1{color: #0F3376; padding: 2vh;}p{font-size: 1.5rem;}.button{display: inline-block; background-color: #e7bd3b; border: none; 
    border-radius: 4px; color: white; padding: 16px 40px; text-decoration: none; font-size: 30px; margin: 2px; cursor: pointer;}
    .button2{background-color: #4286f4;}</style>
	
	    </head>
	    <body> 
		<h1>Lansando a braba pa nois</h1> 
		<p><a href="/?led_r=off"><button class="button button2">REFRESH</button></a></p>
	    </body>
        </html>"""
    
    return html

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 80))
s.listen(5)

TX2 = 17
RX2 = 16

uart = UART(1, 115200)
uart.init(115200, bits=8, parity=None, stop=1, rx=RX2, tx=TX2)

while True:

    conn, addr = s.accept()
    print('Got a connection from %s' % str(addr))
    request = conn.recv(1024)
    request = str(request)
    print('Content = %s' % request)
    led_g_on = request.find('/?led_g=on')
    led_g_off = request.find('/?led_g=off')
    led_r_on = request.find('/?led_r=on')
    led_r_off = request.find('/?led_r=off')

    if led_g_on == 6:
        print('LED GREEN ON')
        led_g.value(1)
    if led_g_off == 6:
        print('LED GREEN OFF')
        led_g.value(0)
    if led_r_on == 6:
        print('LED RED ON')
        led_r.value(1)
    if led_r_off == 6:
        print('LED RED OFF')
        led_r.value(0)

    response = web_page()
    conn.send('HTTP/1.1 200 OK\n')
    conn.send('Content-Type: text/html\n')
    conn.send('Connection: close\n\n')
    conn.sendall(response)
    conn.close()

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
