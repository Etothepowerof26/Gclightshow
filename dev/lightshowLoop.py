#!/usr/bin/python
import RPi.GPIO as GPIO
import importlib, time
import light
importlib.import_module("light")
GPIO.cleanup()
#set GPIO as the numbers of pins
GPIO.setmode(GPIO.BOARD)
#set up pins
pinList = [11,12,13, 15, 16, 18, 22, 7]
for i in pinList:
    GPIO.setup(i, GPIO.OUT) 
    GPIO.output(i, True)
light1=light.Light(pinList[0])
light2=light.Light(pinList[1])
light3=light.Light(pinList[2])
light4=light.Light(pinList[3])
light5=light.Light(pinList[4])
light6=light.Light(pinList[5])
light7=light.Light(pinList[6])
light8=light.Light(pinList[7])

#set up pin array
lightTa=[light3,light4,light5,light6,light7,light8]
#create light show array object with correct GPIO out pins
lightShow1=light.LightShow(1,lightTa,[6,1,1,.5])

for x in range(0,1000):
    lightShow1.oboblink()
    lightShow1.blink(4)
    lightShow1.altBlink()
    lightShow1.bounce()
    lightShow1.rowblink()
    lightShow1.obobblink()