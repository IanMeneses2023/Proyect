from machine import Pin
from machine import ADC
from time import sleep

led= Pin(5,Pin.OUT)
audio= ADC(0)

while True:
  sleep(0.5)
  print(audio.read())
  
gpio.mode(3,gpio.INPUT)

function.havesound (level)
print(level)
end
  
gpio.trig(3,"both",havesound)
