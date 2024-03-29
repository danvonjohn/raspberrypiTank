#packages
from requests.exceptions import ConnectionError
import socket
import requests
import RPi.GPIO as GPIO
import time
import os
import subprocess
import multiprocessing
from gpiozero import CamJamKitRobot  # Import the CamJam GPIO Zero Library 

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
# Set the GPIO Pin mode
GPIO.setup(7, GPIO.OUT)
GPIO.setup(8, GPIO.OUT)
GPIO.setup(9, GPIO.OUT)
GPIO.setup(10, GPIO.OUT)
# Turn all motors off
GPIO.output(7, 0)
GPIO.output(8, 0)
GPIO.output(9, 0)
GPIO.output(10, 0)

robot = CamJamKitRobot() 

# Turn the motors on robot.forward() 
GPIO.output(10,GPIO.HIGH)
GPIO.output(8,GPIO.HIGH)
# Wait for 1 seconds time.sleep(1) 
time.sleep(10)
# Turn the motors off robot.stop()
GPIO.output(10, GPIO.LOW)
GPIO.output(8, GPIO.LOW)
#Motor test
print("Motor test complete")

os.system("sudo service apache2 start")
print("server is starting")

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
#Red
GPIO.setup(18,GPIO.OUT)
print ("Red LED on")
GPIO.output(18,GPIO.HIGH)
time.sleep(1)
print ("Red LED off")
GPIO.output(18,GPIO.LOW)
#Blue
GPIO.setup(17,GPIO.OUT)
print ("Blue LED on")
GPIO.output(17,GPIO.HIGH)
time.sleep(1)
print ("blue LED off")
GPIO.output(17,GPIO.LOW)
time.sleep(0.1)
#Yellow and green
print ("Yellow and Green LED on")
GPIO.output(23,GPIO.HIGH)
GPIO.output(22,GPIO.HIGH)
time.sleep(0.1)
print ("Yellow and Green LED off")
GPIO.output(23,GPIO.LOW)
GPIO.output(22,GPIO.LOW)
time.sleep(0.1)
#Yellow and green
print ("Yellow and Green LED on")
GPIO.output(23,GPIO.HIGH)
GPIO.output(22,GPIO.HIGH)
time.sleep(0.1)
print ("Yellow and Green LED off")
GPIO.output(23,GPIO.LOW)
GPIO.output(22,GPIO.LOW)
#################################

#Connection LED - Internet
#LED - Green
#Pin - 16
#GPIO - 23
def internetConnection():
    try:
       r = requests.get("http://google.com", timeout=1)
    except ConnectionError as e:    # This is the correct syntax
       print (e)
       r = "No response"
       print (r)
       GPIO.output(23,GPIO.LOW)
       time.sleep(1)
       internetConnection()
    else:
        print("Internet Connection")
        GPIO.output(23,GPIO.HIGH)
        time.sleep(1)
        internetConnection()
################################

#Connection LED - Server
#LED - Yellow
#Pin - 15
#GPIO - 22
def serverConnection():
    try:
       r = requests.get("http://localhost/", timeout=1)
    except ConnectionError as e:    # This is the correct syntax
       print (e)
       r = "No response"
       print (r)
       GPIO.output(22,GPIO.LOW)
       time.sleep(1)
       serverConnection()
    else:
        print("Server Connection")
        GPIO.output(22,GPIO.HIGH)
        time.sleep(1)
        serverConnection()
################################

#Shutdown Button
################################

#Shutdown LED Flash
################################

#Battery LED High
################################

#Battery LED Med
################################

#Battery LED Low
################################

#Battery LED Low Flashing
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
        
        
#Multiprocesing the functions
#declare the functions that are to be multiprocessed
p1 = multiprocessing.Process(target=internetConnection,args=[])
p2 = multiprocessing.Process(target=serverConnection,args=[])

#call the multiprocessing functions
if __name__ == '__main__':
    p1.start()
    p2.start()
    p1.join()
    p2.join()
