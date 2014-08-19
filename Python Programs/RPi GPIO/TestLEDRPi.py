import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)

GPIO.setup(11, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)

<<<<<<< HEAD
GPIO.output(18,False)
GPIO.output(12,False)
GPIO.output(16,True)
=======
GPIO.output(12,True)
>>>>>>> a40f4996d09ce6040e18883fc5dc35ce7290c640

while True:
	GPIO.output(11,True)
	GPIO.output(15,True)
	time.sleep(1)
	GPIO.output(11,False)
	GPIO.output(15,False)
        time.sleep(1)

