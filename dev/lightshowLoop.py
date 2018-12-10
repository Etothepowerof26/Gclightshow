#!/usr/bin/python
import RPi.GPIO as GPIO
import importlib, time
import light
#  sudo python /home/Gclightshow/dev/lightshowLoop.py &
importlib.import_module("light")
GPIO.cleanup()
#set GPIO as the numbers of pins
GPIO.setmode(GPIO.BOARD)
#set up pins
pinList = [11,12,13, 15, 16, 18, 22, 7]
for i in pinList:
    GPIO.setup(i, GPIO.OUT) 
    GPIO.output(i, True)
light1=light.Light(pinList[0],"1")
light2=light.Light(pinList[1],"2")
light3=light.Light(pinList[7],"3")
light4=light.Light(pinList[6],"4")
light5=light.Light(pinList[5],"5")
light6=light.Light(pinList[4],"6")
light7=light.Light(pinList[3],"7")
light8=light.Light(pinList[2],"8")

#set up pin array
lightTa=[light3,light4,light5,light6,light7,light8]
#create light show array object with correct GPIO out pins
lightShow1=light.LightShow(1,lightTa,[1,1,1,.5])
try:
    for x in range(0,1000):
        lightShow1.gcBlink()
        lightShow1.gcBlink()
        lightShow1.gcBlink()
        lightShow1.gcBlink()
        time.sleep(2)
        
        lightShow1.oboblink()
        lightShow1.blink(4)
        lightShow1.altBlink(4)
        lightShow1.bounce()
        lightShow1.rowblink()
        lightShow1.obobblink()
        lightShow1.offP()
        time.sleep(180)
except KeyboardInterrupt:
  print("Quit")

  # Reset GPIO settings
  GPIO.cleanup()