#!/usr/bin/python
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

# init list with pin numbers

pinList = [2, 3, 4, 17, 27, 22, 10, 9]

# loop through pins and set mode and state to 'low'

for i in pinList: 
    GPIO.setup(i, GPIO.OUT) 
    GPIO.output(i, GPIO.HIGH)

# time to sleep between operations in the main loop

SleepTimeL = 0.1

# main loop

try:
   count = 3
   while (count > 0):

      print('   The count is:', count)

      for i in pinList:
         GPIO.output(i, GPIO.LOW)
         time.sleep(SleepTimeL);

      pinList.reverse()

      for i in pinList:
         GPIO.output(i, GPIO.HIGH)
         time.sleep(SleepTimeL);

      pinList.reverse()
      count = count - 1


# End program cleanly with keyboard
except KeyboardInterrupt:
  print("Quit")

  # Reset GPIO settings
GPIO.cleanup()


# find more information on this script at
# http://youtu.be/oaf_zQcrg7g
import pygame
pygame.mixer.init()
pygame.mixer.music.load("RonettesSleighBells.mp3")
pygame.mixer.music.play()
while pygame.mixer.music.get_busy() == True:
    continue
