import pygame
import RPi.GPIO as GPIO
pygame.init()

#setup pins
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(23,GPIO.OUT)
GPIO.setup(22,GPIO.OUT)
GPIO.setup(18,GPIO.OUT)
GPIO.setup(17,GPIO.OUT)

#colours 
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

#display screen 
dis = pygame.display.set_mode((300, 300))
pygame.display.set_caption('TANK')
 
game_over = False

#start position 
x1 = 150
y1 = 150

#movement changes
x1_change = 0       
y1_change = 0
 
clock = pygame.time.Clock()
 
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        #press actions
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x1_change = -10
                y1_change = 0
                x1 += x1_change
                y1 += y1_change
                GPIO.output(17,GPIO.HIGH)
            elif event.key == pygame.K_RIGHT:
                x1_change = 10
                y1_change = 0
                x1 += x1_change
                y1 += y1_change
                GPIO.output(22,GPIO.HIGH)
            elif event.key == pygame.K_UP:
                y1_change = -10
                x1_change = 0
                x1 += x1_change
                y1 += y1_change
                GPIO.output(23,GPIO.HIGH)
            elif event.key == pygame.K_DOWN:
                y1_change = 10
                x1_change = 0
                x1 += x1_change
                y1 += y1_change
                GPIO.output(18,GPIO.HIGH)
        #release actions
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                #reset position
                x1 = 150
                y1 = 150
                GPIO.output(17,GPIO.LOW)
            elif event.key == pygame.K_RIGHT:
                x1 = 150
                y1 = 150
                GPIO.output(22,GPIO.LOW)
            elif event.key == pygame.K_UP:
                x1 = 150
                y1 = 150
                GPIO.output(23,GPIO.LOW)
            elif event.key == pygame.K_DOWN:
                x1 = 150
                y1 = 150
                GPIO.output(18,GPIO.LOW)

    dis.fill(white)
    pygame.draw.rect(dis, black, [x1, y1, 10, 10])
    pygame.display.update()
    #game speed
    clock.tick(300)
 
pygame.quit()
quit()
