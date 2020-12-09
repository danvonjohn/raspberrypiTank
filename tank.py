#packages
from requests.exceptions import ConnectionError
import socket
import requests
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

#Boot up
#Green on
GPIO.setup(23,GPIO.OUT)
print ("Green LED on")
GPIO.output(23,GPIO.HIGH)
time.sleep(1)
print ("Green LED off")
GPIO.output(23,GPIO.LOW)
#Yellow
GPIO.setup(22,GPIO.OUT)
print ("Yellow LED on")
GPIO.output(22,GPIO.HIGH)
time.sleep(1)
print ("Yellow LED off")
GPIO.output(22,GPIO.LOW)
time.sleep(0.1)
#Yellow and green
print ("Yellow and Green LED on")
GPIO.output(23,GPIO.HIGH)
GPIO.output(22,GPIO.HIGH)
time.sleep(1)
print ("Yellow and Green LED off")
GPIO.output(23,GPIO.LOW)
GPIO.output(22,GPIO.LOW)
#################################

#Connection LED - Internet
#LED - Green
#Pin - 16
#GPIO - 23

def internetConnection():
    IPaddress=socket.gethostbyname(socket.gethostname())
    if IPaddress=="127.0.0.1":
        print ("No internet connection")
        GPIO.output(23,GPIO.LOW)
        time.sleep(1)
        internetConnection()
    else:
        print("Internet connection")
        GPIO.output(23,GPIO.HIGH)
        time.sleep(1)
        internetConnection()
internetConnection()
################################

#Connection LED - Server

################################

#Shutdown Button
################################

#Shutdown LED Flash
################################

#Battery LED High
#LED - Yellow
#Pin - 15
#GPIO - 22
################################

#Battery LED Med
#LED - Yellow
#Pin - 15
#GPIO - 22
################################

#Battery LED Low
#LED - Yellow
#Pin - 15
#GPIO - 22
################################

#Battery LED Low Flashing
#LED - Yellow
#Pin - 15
#GPIO - 22
################################

#Forward
################################

#Turn left
#LED - Red
#Pin - 12
#GPIO - 18
################################

#Turn Right
#LED - Blue
#Pin - 11
#GPIO - 17
################################