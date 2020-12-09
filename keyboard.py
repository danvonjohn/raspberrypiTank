import pygame, sys
from pygame.locals import *
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(23,GPIO.OUT)

pygame.init()
BLACK = (0,0,0)
WIDTH = 100
HEIGHT = 100
pp
windowSurface.fill(BLACK)
x = 0
while True:
   for event in pygame.event.get():
      if event.type == QUIT:
            pygame.quit()
            sys.exit()
      if event.type == KEYDOWN:
         key = event.key
         if key == pygame.K_p:
            if x == 0:
               GPIO.output(23,GPIO.HIGH)
               x = 1
            else:
               GPIO.output(23,GPIO.LOW)
               x = 0
