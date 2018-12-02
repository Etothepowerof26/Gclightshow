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
    GPIO.output(i, GPIO.HIGH)

# time inbetween each action of light
SleepTimeM = 1000
# main loop
#time.sleep(SleepTimeM)


# Tries to toggle a light.
# Inputs: 1 for on, 0 for off (True==1 and False==0), anything
# else will fallback to off.
def lightToggle(light, onOrOff):
    pinNumber = pinList[(light-1)]
    
    #PIO.output(pinNumber, (onOrOff == 1 or onOrOff == True) and GPIO.LOW or ((onOrOff == 1 or onOrOff == True) and GPIO.HIGH or GPIO.LOW)

    #print("Light " + str(light) + " is now " + ((onOrOff == 1 or onOrOff == True) and "ON" or ((onOrOff == 1 or onOrOff == True) and GPIO.HIGH or GPIO.LOW))
    if(onOrOff == 1):
        #light on
        GPIO.output(pinNumber, GPIO.LOW)
        print("Light " + str(light) + " is now ON")
    elif(onOrOff==0):
        GPIO.output(pinNumber, GPIO.HIGH)
        print("Light " + str(light) + " is now OFF")
    else:
        print("Invalid ON or OFF position")
        

try:
    for i in range(1):
        # turn on lights
        lightToggle(3,1)
        lightToggle(4,1)
        lightToggle(5,1)
        lightToggle(6,1)
        lightToggle(7,1)
        lightToggle(8,1)
        time.sleep(SleepTimeM)
        # turn off lights
        lightToggle(3,0)
        lightToggle(4,0)
        lightToggle(5,0)
        lightToggle(6,0)
        time.sleep(SleepTimeM)
    print("Quit")
    
# End program cleanly with keyboard
except KeyboardInterrupt:
  print("Quit")

  # Reset GPIO settings
  GPIO.cleanup()


# find more information on this script at
# http://youtu.be/oaf_zQcrg7g
