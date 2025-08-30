# importing pygame module
import pygame
import pigpio
from pygame.locals import *

# importing sys module
import sys

PinFR = 3     #Front Right Motor
PinFL = 15    #Front Left Motor
PinBR = 27    #Back Right Motor
PinBL = 10    #Back Left Motor

pwm = pigpio.pi()
    
def forward(s1 = 2000, s2 = 1000):
    pwm.set_servo_pulsewidth(PinFR, s1) #anti-clockwise
    pwm.set_servo_pulsewidth(PinFL, s2) #clockwise
    pwm.set_servo_pulsewidth(PinBR, s2) #anti-clockwise
    pwm.set_servo_pulsewidth(PinBL, s1) #clockwise
    
def backward(s1 = 2000, s2 = 1000):
    pwm.set_servo_pulsewidth(PinFR, s2) #anti-clockwise
    pwm.set_servo_pulsewidth(PinFL, s1) #clockwise
    pwm.set_servo_pulsewidth(PinBR, s1) #anti-clockwise
    pwm.set_servo_pulsewidth(PinBL, s2) #clockwise
    
def right():
    pwm.set_servo_pulsewidth(PinFR, 2000) #anti-clockwise
    pwm.set_servo_pulsewidth(PinFL, 2000) #clockwise
    pwm.set_servo_pulsewidth(PinBR, 2000) #anti-clockwise
    pwm.set_servo_pulsewidth(PinBL, 2000) #clockwise
    
def left():
    pwm.set_servo_pulsewidth(PinFR, 1000) #anti-clockwise
    pwm.set_servo_pulsewidth(PinFL, 1000) #clockwise
    pwm.set_servo_pulsewidth(PinBR, 1000) #anti-clockwise
    pwm.set_servo_pulsewidth(PinBL, 1000) #clockwise
    
def stop():
    pwm.set_servo_pulsewidth(PinFR, 0) #anti-clockwise
    pwm.set_servo_pulsewidth(PinFL, 0) #clockwise
    pwm.set_servo_pulsewidth(PinBR, 0) #anti-clockwise
    pwm.set_servo_pulsewidth(PinBL, 0) #clockwise
    

# initialising pygame
pygame.init()

# creating display
display = pygame.display.set_mode((300, 300))

# creating a running loop
while True:
	# creating a loop to check events that
	# are occurring
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
		
		# checking if keydown event happened ore not
		if event.type == pygame.KEYDOWN:
			# checking if key "W" was pressed
			if event.key == pygame.K_w:
				forward()
			
			# checking if key "S" was pressed
			if event.key == pygame.K_s:
				backward()
			
			# checking if key "D" was pressed
			if event.key == pygame.K_d:
				right()
			
			# checking if key "A" was pressed
			if event.key == pygame.K_a:
				left()
				
			if event.key == pygame.K_ESCAPE:
				stop()
				break
						
		if event.type == pygame.KEYUP:
 				stop()

sys.exit()
pygame.exit()

