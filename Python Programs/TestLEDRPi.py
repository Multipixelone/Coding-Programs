import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)

	GPIO.setup(18, GPIO.OUT)
	GPIO.setup(12, GPIO.OUT)

GPIO.output(18,False)

while True:
	GPIO.output(18,True)
	GPIO.output(12,True)
	time.sleep(1)
	GPIO.output(18,False)
	GPIO.output(12,False)
        time.sleep(1)
while True:
	
