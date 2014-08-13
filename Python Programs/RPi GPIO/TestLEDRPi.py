from random import randint
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)

GPIO.setup(18, GPIO.OUT)
GPIO.setup(12, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)

GPIO.output(18,False)

while True:
	GPIO.output(18,True)
	GPIO.output(12,True)
	time.sleep(randint(0,2)
	GPIO.output(18,False)
	GPIO.output(12,False)
        time.sleep(randint(0,2))
while True:
	GPIO.output(16,True)
	time.sleep(randint(0,4))
	GPIO.output(16,False)
	time.sleep(randint(0,4)