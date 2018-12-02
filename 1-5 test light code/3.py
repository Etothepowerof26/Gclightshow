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

standardSpeed=.7
# loop through pins and set mode and state to 'low'
for i in pinList:
    GPIO.setup(i, GPIO.OUT) 
    GPIO.output(i, True)

# time inbetween each action of light
SleepTimeM = .2
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

def bounce(numTimes):
    light1=3
    light2=4
    light3=5
    light4=6
    light5=7
    light6=8
    SleepTimeQ=standardSpeed*(3/5)
    for x in ("b"*numTimes):
        lightToggle(light1,0)
        lightToggle(light2,0)
        lightToggle(light3,0)
        lightToggle(light4,0)
        lightToggle(light5,0)
        lightToggle(light6,0)
        time.sleep(SleepTimeQ);
        

        lightToggle(light1,1)
        lightToggle(light2,0)
        lightToggle(light3,0)
        lightToggle(light4,0)
        lightToggle(light5,0)
        lightToggle(light6,0)
        time.sleep(SleepTimeQ);


        lightToggle(light1,0)
        lightToggle(light2,1)
        lightToggle(light3,0)
        lightToggle(light4,0)
        lightToggle(light5,0)
        lightToggle(light6,0)
        time.sleep(SleepTimeQ);

        lightToggle(light1,0)
        lightToggle(light2,0)
        lightToggle(light3,1)
        lightToggle(light4,0)
        lightToggle(light5,0)
        lightToggle(light6,0)
        time.sleep(SleepTimeQ);

        lightToggle(light1,0)
        lightToggle(light2,0)
        lightToggle(light3,0)
        lightToggle(light4,1)
        lightToggle(light5,0)
        lightToggle(light6,0)
        time.sleep(SleepTimeQ);

        lightToggle(light1,0)
        lightToggle(light2,0)
        lightToggle(light3,0)
        lightToggle(light4,0)
        lightToggle(light5,1)
        lightToggle(light6,0)
        time.sleep(SleepTimeQ);

        lightToggle(light1,0)
        lightToggle(light2,0)
        lightToggle(light3,0)
        lightToggle(light4,0)
        lightToggle(light5,0)
        lightToggle(light6,1)
        time.sleep(SleepTimeQ);

        lightToggle(light1,0)
        lightToggle(light2,0)
        lightToggle(light3,0)
        lightToggle(light4,0)
        lightToggle(light5,1)
        lightToggle(light6,0)
        time.sleep(SleepTimeQ);

        lightToggle(light1,0)
        lightToggle(light2,0)
        lightToggle(light3,0)
        lightToggle(light4,1)
        lightToggle(light5,0)
        lightToggle(light6,0)
        time.sleep(SleepTimeQ);

        lightToggle(light1,0)
        lightToggle(light2,0)
        lightToggle(light3,1)
        lightToggle(light4,0)
        lightToggle(light5,0)
        lightToggle(light6,0)
        time.sleep(SleepTimeQ);

        lightToggle(light1,0)
        lightToggle(light2,1)
        lightToggle(light3,0)
        lightToggle(light4,0)
        lightToggle(light5,0)
        lightToggle(light6,0)
        time.sleep(SleepTimeQ);

        lightToggle(light1,1)
        lightToggle(light2,0)
        lightToggle(light3,0)
        lightToggle(light4,0)
        lightToggle(light5,0)
        lightToggle(light6,0)
        time.sleep(SleepTimeQ);

def quickBlink(numTimes):
    '''quickly blink specified light'''
    light1=3
    light2=4
    light3=5
    light4=6
    light5=7
    light6=8
    SleepTimeQ=standardSpeed/5
    for x in ("b"*numTimes):
        lightToggle(light1,0)
        lightToggle(light2,0)
        lightToggle(light3,0)
        lightToggle(light4,0)
        lightToggle(light5,0)
        lightToggle(light6,0)
        time.sleep(SleepTimeQ);
        

        lightToggle(light1,1)
        lightToggle(light2,1)
        lightToggle(light3,1)
        lightToggle(light4,1)
        lightToggle(light5,1)
        lightToggle(light6,1)
        time.sleep(SleepTimeQ);


        lightToggle(light1,0)
        lightToggle(light2,0)
        lightToggle(light3,0)
        lightToggle(light4,0)
        lightToggle(light5,0)
        lightToggle(light6,0)
        time.sleep(SleepTimeQ);

def quickrowBlink(numTimes):
    '''quickly blink specified light'''
    light1=3
    light2=4
    light3=5
    light4=6
    light5=7
    light6=8
    SleepTimeQ=standardSpeed/5
    for x in ("b"*numTimes):
        lightToggle(light1,0)
        time.sleep(SleepTimeQ);
        lightToggle(light2,0)
        time.sleep(SleepTimeQ);
        lightToggle(light3,0)
        time.sleep(SleepTimeQ);
        lightToggle(light4,0)
        time.sleep(SleepTimeQ);
        lightToggle(light5,0)
        time.sleep(SleepTimeQ);
        lightToggle(light6,0)
        time.sleep(SleepTimeQ);
        

        lightToggle(light1,1)
        time.sleep(SleepTimeQ);
        lightToggle(light2,1)
        time.sleep(SleepTimeQ);
        lightToggle(light3,1)
        time.sleep(SleepTimeQ);
        lightToggle(light4,1)
        time.sleep(SleepTimeQ);
        lightToggle(light5,1)
        time.sleep(SleepTimeQ);
        lightToggle(light6,1)
        time.sleep(SleepTimeQ);



        lightToggle(light1,0)
        time.sleep(SleepTimeQ);
        lightToggle(light2,0)
        time.sleep(SleepTimeQ);
        lightToggle(light3,0)
        time.sleep(SleepTimeQ);
        lightToggle(light4,0)
        time.sleep(SleepTimeQ);
        lightToggle(light5,0)
        time.sleep(SleepTimeQ);
        lightToggle(light6,0)
        time.sleep(SleepTimeQ);

def closeP():
    '''at end of program - turn off all lights'''
    lightToggle(3,0)
    lightToggle(4,0)
    lightToggle(5,0)
    lightToggle(6,0)
    lightToggle(7,0)
    lightToggle(8,0)
    print("exit with no errors")
    
def altBlink(num):
    '''alternate between sets of lights'''
    light1=3
    light2=4
    light3=5
    light4=6
    light5=7
    light6=8
    for x in ("b"*num):
        SleepTimeA=2*standardSpeed
        lightToggle(light1,0)
        lightToggle(light2,1)
        lightToggle(light3,0)
        lightToggle(light4,1)
        lightToggle(light5,0)
        lightToggle(light6,1)
        time.sleep(SleepTimeA);
        
        lightToggle(light1,1)
        lightToggle(light2,0)
        lightToggle(light3,1)
        lightToggle(light4,0)
        lightToggle(light5,1)
        lightToggle(light6,0)
        time.sleep(SleepTimeA);
        
        lightToggle(light1,0)
        lightToggle(light2,1)
        lightToggle(light3,0)
        lightToggle(light4,1)
        lightToggle(light5,0)
        lightToggle(light6,1)
        # turn off lights

def blink(num,speed):
    light1=3
    light2=4
    light3=5
    light4=6
    light5=7
    light6=8
    for x in ("b"*num):
        SleepTimeA=speed
        lightToggle(light1,0)
        lightToggle(light2,0)
        lightToggle(light3,0)
        lightToggle(light4,0)
        lightToggle(light5,0)
        lightToggle(light6,0)
        time.sleep(SleepTimeA);
        
        lightToggle(light1,1)
        lightToggle(light2,1)
        lightToggle(light3,1)
        lightToggle(light4,1)
        lightToggle(light5,1)
        lightToggle(light6,1)
        time.sleep(SleepTimeA);
        

def gradBlink(num):
    '''turn on lights gradually one by one'''
    light1=3
    light2=4
    light3=5
    light4=6
    light5=7
    light6=8
    for x in ("b"*num):
        SleepTimeA=standardSpeed
        lightToggle(light1,0)
        lightToggle(light2,0)
        lightToggle(light3,0)
        lightToggle(light4,0)
        lightToggle(light5,0)
        lightToggle(light6,0)
        time.sleep(SleepTimeA);
        
        lightToggle(light1,1)
        lightToggle(light2,0)
        lightToggle(light3,0)
        lightToggle(light4,0)
        lightToggle(light5,0)
        lightToggle(light6,0)
        time.sleep(SleepTimeA);
        
        lightToggle(light1,1)
        lightToggle(light2,1)
        lightToggle(light3,0)
        lightToggle(light4,0)
        lightToggle(light5,0)
        lightToggle(light6,0)
        time.sleep(SleepTimeA);
        
        lightToggle(light1,1)
        lightToggle(light2,1)
        lightToggle(light3,1)
        lightToggle(light4,0)
        lightToggle(light5,0)
        lightToggle(light6,0)
        time.sleep(SleepTimeA);

        lightToggle(light1,1)
        lightToggle(light2,1)
        lightToggle(light3,1)
        lightToggle(light4,1)
        lightToggle(light5,0)
        lightToggle(light6,0)
        time.sleep(SleepTimeA);
        

        lightToggle(light1,1)
        lightToggle(light2,1)
        lightToggle(light3,1)
        lightToggle(light4,1)
        lightToggle(light5,1)
        lightToggle(light6,0)
        time.sleep(SleepTimeA);


        lightToggle(light1,1)
        lightToggle(light2,1)
        lightToggle(light3,1)
        lightToggle(light4,1)
        lightToggle(light5,1)
        lightToggle(light6,1)
        time.sleep(SleepTimeA);

        lightToggle(light1,1)
        lightToggle(light2,1)
        lightToggle(light3,1)
        lightToggle(light4,1)
        lightToggle(light5,1)
        lightToggle(light6,0)
        time.sleep(SleepTimeA);        

        lightToggle(light1,1)
        lightToggle(light2,1)
        lightToggle(light3,1)
        lightToggle(light4,1)
        lightToggle(light5,0)
        lightToggle(light6,0)
        time.sleep(SleepTimeA);

        lightToggle(light1,1)
        lightToggle(light2,1)
        lightToggle(light3,1)
        lightToggle(light4,0)
        lightToggle(light5,0)
        lightToggle(light6,0)
        time.sleep(SleepTimeA);

        lightToggle(light1,1)
        lightToggle(light2,1)
        lightToggle(light3,0)
        lightToggle(light4,0)
        lightToggle(light5,0)
        lightToggle(light6,0)
        time.sleep(SleepTimeA);

        lightToggle(light1,1)
        lightToggle(light2,0)
        lightToggle(light3,0)
        lightToggle(light4,0)
        lightToggle(light5,0)
        lightToggle(light6,0)
        time.sleep(SleepTimeA);

        lightToggle(light1,0)
        lightToggle(light2,0)
        lightToggle(light3,0)
        lightToggle(light4,0)
        lightToggle(light5,0)
        lightToggle(light6,0)
        time.sleep(SleepTimeA);        

def gradbBlink(num):
    '''gradBlink but backwards'''
    light1=3
    light2=4
    light3=5
    light4=6
    light5=7
    light6=8
    for x in ("b"*num):
        SleepTimeA=standardSpeed
        lightToggle(light1,0)
        lightToggle(light2,0)
        lightToggle(light3,0)
        lightToggle(light4,0)
        lightToggle(light5,0)
        lightToggle(light6,0)
        time.sleep(SleepTimeA);
        
        lightToggle(light1,0)
        lightToggle(light2,0)
        lightToggle(light3,0)
        lightToggle(light4,0)
        lightToggle(light5,0)
        lightToggle(light6,1)
        time.sleep(SleepTimeA);
        
        lightToggle(light1,0)
        lightToggle(light2,0)
        lightToggle(light3,0)
        lightToggle(light4,0)
        lightToggle(light5,1)
        lightToggle(light6,1)
        time.sleep(SleepTimeA);
        
        lightToggle(light1,0)
        lightToggle(light2,0)
        lightToggle(light3,0)
        lightToggle(light4,1)
        lightToggle(light5,1)
        lightToggle(light6,1)
        time.sleep(SleepTimeA);

        lightToggle(light1,0)
        lightToggle(light2,0)
        lightToggle(light3,1)
        lightToggle(light4,1)
        lightToggle(light5,1)
        lightToggle(light6,1)
        time.sleep(SleepTimeA);
        

        lightToggle(light1,0)
        lightToggle(light2,1)
        lightToggle(light3,1)
        lightToggle(light4,1)
        lightToggle(light5,1)
        lightToggle(light6,1)
        time.sleep(SleepTimeA);

        lightToggle(light1,1)
        lightToggle(light2,1)
        lightToggle(light3,1)
        lightToggle(light4,1)
        lightToggle(light5,1)
        lightToggle(light6,1)
        time.sleep(SleepTimeA);


        lightToggle(light1,0)
        lightToggle(light2,1)
        lightToggle(light3,1)
        lightToggle(light4,1)
        lightToggle(light5,1)
        lightToggle(light6,1)
        time.sleep(SleepTimeA);

        lightToggle(light1,0)
        lightToggle(light2,0)
        lightToggle(light3,1)
        lightToggle(light4,1)
        lightToggle(light5,1)
        lightToggle(light6,1)
        time.sleep(SleepTimeA);        

        lightToggle(light1,0)
        lightToggle(light2,0)
        lightToggle(light3,0)
        lightToggle(light4,1)
        lightToggle(light5,1)
        lightToggle(light6,1)
        time.sleep(SleepTimeA);

        lightToggle(light1,0)
        lightToggle(light2,0)
        lightToggle(light3,0)
        lightToggle(light4,0)
        lightToggle(light5,1)
        lightToggle(light6,1)
        time.sleep(SleepTimeA);

        lightToggle(light1,0)
        lightToggle(light2,0)
        lightToggle(light3,0)
        lightToggle(light4,0)
        lightToggle(light5,0)
        lightToggle(light6,1)


        
#start indicator
# main loop
try:
  for x in range(20000):
##        # turn on lights
      quickBlink(1)
      quickrowBlink(1)
      bounce(5)
      gradBlink(1)
      gradbBlink(1)
      blink(1,1) #(times,speed in seconds)
      altBlink(5)
      #

      #quickBlink(3,3)
      #quickBlink(3,3)
      #quickBlink(3,3)
      #quickBlink(3,3)
      closeP()
 

# End program cleanly with keyboard
except KeyboardInterrupt:
  print("Quit")

  # Reset GPIO settings
  GPIO.cleanup()


# find more information on this script at
# http://youtu.be/oaf_zQcrg7g
