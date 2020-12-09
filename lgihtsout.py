import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
#Lights out
GPIO.setup(23,GPIO.OUT)
GPIO.setup(22,GPIO.OUT)
GPIO.setup(18,GPIO.OUT)
GPIO.setup(17,GPIO.OUT)

GPIO.output(23,GPIO.LOW)
GPIO.output(22,GPIO.LOW)
GPIO.output(18,GPIO.LOW)
GPIO.output(17,GPIO.LOW)