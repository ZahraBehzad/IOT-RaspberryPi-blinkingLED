import RPi.GPIO as GPIO
from time import sleep

LED_PIN = 18
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)

while True:
    GPIO.output(LED_PIN, GPIO.HIGH)
    sleep(1)
    GPIO.output(LED_PIN, GPIO.LOW)