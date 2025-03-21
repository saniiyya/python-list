# Write your code here :-)
from machine import Pin, PWM
enA = PWM(Pin(15))
in1 = Pin(12,Pin.OUT)
in2 = Pin (13,Pin.OUT)

enA.freq(1000)
enA.duty(512)

while True :
    in1.value(1)
    in2.value(0)
    time.sleep(2)
    in1.value (0)
    in2.value(1)
    time.sleep(2)
