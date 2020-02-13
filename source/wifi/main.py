def web_page():
    if led_g.value() == 1:
        gpio_state_g="ON"
    else:
        gpio_state_g="OFF"
  
    html = """<html><head> <title>ESP Web Server</title> <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="icon" href="data:,"> <style>html{font-family: Helvetica; display:inline-block; margin: 0px auto; text-align: center;}
    h1{color: #0F3376; padding: 2vh;}p{font-size: 1.5rem;}.button{display: inline-block; background-color: #e7bd3b; border: none; 
    border-radius: 4px; color: white; padding: 16px 40px; text-decoration: none; font-size: 30px; margin: 2px; cursor: pointer;}
    .button2{background-color: #4286f4;}</style></head><body> <h1>ESP Web Server</h1> 
    <p>GPIO state: <strong>""" + gpio_state_g + """</strong></p><p><a href="/?led_g=on"><button class="button">ON</button></a></p>
    <p><a href="/?led_g=off"><button class="button button2">OFF</button></a></p></body></html>"""
    return html



'''
    <<HELLO WORD CODE>>

    html = """<html><head><meta name="viewport" content="width=device-width, initial-scale=1"></head>
    <body><h1>Hello, World!</h1></body></html>"""
    return html
'''

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 80))
s.listen(5)

while True:
    conn, addr = s.accept()
    print('Got a connection from %s' % str(addr))
    request = conn.recv(1024)
    request = str(request)
    print('Content = %s' % request)
    led_g_on = request.find('/?led_g=on')
    led_g_off = request.find('/?led_g=off')
    if led_g_on == 6:
        print('LED ON')
        led_g.value(1)
    if led_g_off == 6:
        print('LED OFF')
        led_g.value(0)
    response = web_page()
    conn.send('HTTP/1.1 200 OK\n')
    conn.send('Content-Type: text/html\n')
    conn.send('Connection: close\n\n')
    conn.sendall(response)
    conn.close()
