from machine import ADC
from machine import Pin
import utime

sensor = ADC(4)
led = Pin(0,Pin.OUT)
while True:
    valor = sensor.read_u16()*3.3/65535
    temp = 27-(valor-0.706)/0.001721
    print(temp)
    if temp >= 31:
        led.value(1)
    else:
        led.value(0)        
    utime.sleep(1)
    