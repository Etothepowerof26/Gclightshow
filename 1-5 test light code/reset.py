#!/usr/bin/python
import RPi.GPIO as GPIO
import time
GPIO.cleanup()
GPIO.setmode(GPIO.BOARD)

# init list with pin numbers

#pinList = [2, 3, 4, 17, 27, 22, 10, 9]
pinList = [11,12,13, 15, 16, 18, 22, 7]
#          1 2  3   4   5   6   7
# plug numbers

# loop through pins and set mode and state to 'low'

for i in pinList:
    GPIO.setup(i, GPIO.OUT) 
    GPIO.output(i, True)

# time inbetween each action of light
SleepTimeM = .2
# main loop
time.sleep(SleepTimeM)

def lightToggle(light, onOrOff):
    pinNumber=pinList[(light-1)]
    if(onOrOff==1):
        #light on
        GPIO.output(pinNumber, False)
        print(str(light)+"is on")
    elif(onOrOff==0):
        GPIO.output(pinNumber, True)
        print(str(light)+"is off")
    else:
        print("Invalid ON or OFF position")
try:
    lightToggle(3,0)
    #time.sleep(SleepTimeM);
    lightToggle(4,0)
    #time.sleep(SleepTimeM);
    lightToggle(5,0)
    #time.sleep(SleepTimeM);
    lightToggle(6,0)

# End program cleanly with keyboard
except KeyboardInterrupt:
  print("Quit")

  # Reset GPIO settings
  GPIO.cleanup()


# find more information on this script at
# http://youtu.be/oaf_zQcrg7g
