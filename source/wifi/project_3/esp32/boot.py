# Complete project details at https://RandomNerdTutorials.com

import network

try:
  import usocket as socket
except:
  import socket

from machine import Pin

import esp
esp.osdebug(None)

import gc
gc.collect()

ssid = 'NotAVirus'
password = '123456789'

ap = network.WLAN(network.AP_IF)
ap.active(True)
ap.config(essid=ssid, password=password)

while ap.active() == False:
  pass

print('Connection successful')
print(ap.ifconfig())

led_r = Pin(22, Pin.OUT)
led_g = Pin(21, Pin.OUT)
