import gpiozero
import time

red_led = PWM_LED(15)
blue_led = LED(12)

red_led.on()
red_led.off()