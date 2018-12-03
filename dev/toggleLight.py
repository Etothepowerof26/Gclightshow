'''Toggle the lights'''
import RPi.GPIO as GPIO
import time
# init list with pin numbers
#pinList = [2, 3, 4, 17, 27, 22, 10, 9]
pinList = [11,12,13, 15, 16, 18, 22, 7]
#          1   2  3   4   5   6   7 ,8
# plug numbers
lightlist = [3,4,5,6,7,8]
SleepTimeS = 1
SleepTime = [6,1,1]
light1=lightlist[0]
light2=lightlist[1]
light3=lightlist[2]
light4=lightlist[3]
light5=lightlist[4]
light6=lightlist[5]

# loop through pins and set mode and state to 'low'
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

def bounce(numTimes,SleepTimeQ=(SleepTimeS/SleepTime[0])):
    for x in ("b"*numTimes):
        lightToggle(light1,0)
        lightToggle(light2,0)
        lightToggle(light3,0)
        lightToggle(light4,0)
        lightToggle(light5,0)
        lightToggle(light6,0)
        time.sleep(SleepTimeQ)
        

        lightToggle(light1,1)
        lightToggle(light2,0)
        lightToggle(light3,0)
        lightToggle(light4,0)
        lightToggle(light5,0)
        lightToggle(light6,0)
        time.sleep(SleepTimeQ)


        lightToggle(light1,0)
        lightToggle(light2,1)
        lightToggle(light3,0)
        lightToggle(light4,0)
        lightToggle(light5,0)
        lightToggle(light6,0)
        time.sleep(SleepTimeQ) 

        lightToggle(light1,0)
        lightToggle(light2,0)
        lightToggle(light3,1)
        lightToggle(light4,0)
        lightToggle(light5,0)
        lightToggle(light6,0)
        time.sleep(SleepTimeQ) 

        lightToggle(light1,0)
        lightToggle(light2,0)
        lightToggle(light3,0)
        lightToggle(light4,1)
        lightToggle(light5,0)
        lightToggle(light6,0)
        time.sleep(SleepTimeQ) 

        lightToggle(light1,0)
        lightToggle(light2,0)
        lightToggle(light3,0)
        lightToggle(light4,0)
        lightToggle(light5,1)
        lightToggle(light6,0)
        time.sleep(SleepTimeQ) 

        lightToggle(light1,0)
        lightToggle(light2,0)
        lightToggle(light3,0)
        lightToggle(light4,0)
        lightToggle(light5,0)
        lightToggle(light6,1)
        time.sleep(SleepTimeQ) 

        lightToggle(light1,0)
        lightToggle(light2,0)
        lightToggle(light3,0)
        lightToggle(light4,0)
        lightToggle(light5,1)
        lightToggle(light6,0)
        time.sleep(SleepTimeQ) 

        lightToggle(light1,0)
        lightToggle(light2,0)
        lightToggle(light3,0)
        lightToggle(light4,1)
        lightToggle(light5,0)
        lightToggle(light6,0)
        time.sleep(SleepTimeQ) 

        lightToggle(light1,0)
        lightToggle(light2,0)
        lightToggle(light3,1)
        lightToggle(light4,0)
        lightToggle(light5,0)
        lightToggle(light6,0)
        time.sleep(SleepTimeQ) 

        lightToggle(light1,0)
        lightToggle(light2,1)
        lightToggle(light3,0)
        lightToggle(light4,0)
        lightToggle(light5,0)
        lightToggle(light6,0)
        time.sleep(SleepTimeQ) 

        lightToggle(light1,1)
        lightToggle(light2,0)
        lightToggle(light3,0)
        lightToggle(light4,0)
        lightToggle(light5,0)
        lightToggle(light6,0)
        time.sleep(SleepTimeQ) 

def quickBlink(numTimes):
    '''quickly blink specified light'''
    light1=3
    light2=4
    light3=5
    light4=6
    light5=7
    light6=8
    SleepTimeQ=.05
    for x in ("b"*numTimes):
        lightToggle(light1,0)
        lightToggle(light2,0)
        lightToggle(light3,0)
        lightToggle(light4,0)
        lightToggle(light5,0)
        lightToggle(light6,0)
        time.sleep(SleepTimeQ) 
        

        lightToggle(light1,1)
        lightToggle(light2,1)
        lightToggle(light3,1)
        lightToggle(light4,1)
        lightToggle(light5,1)
        lightToggle(light6,1)
        time.sleep(SleepTimeQ) 


        lightToggle(light1,0)
        lightToggle(light2,0)
        lightToggle(light3,0)
        lightToggle(light4,0)
        lightToggle(light5,0)
        lightToggle(light6,0)
        time.sleep(SleepTimeQ) 

def quickrowBlink(numTimes):
    '''quickly blink specified light'''
    light1=lightlist[0]
    light2=lightlist[1]
    light3=lightlist[2]
    light4=lightlist[3]
    light5=lightlist[4]
    light6=lightlist[5]
    #relay breaking times below
    #SleepTimeQ=.05
    SleepTimeQ=SleepTimeS/SleepTime[1]
    for x in ("b"*numTimes):
        lightToggle(light1,0)
        time.sleep(SleepTimeQ) 
        lightToggle(light2,0)
        time.sleep(SleepTimeQ) 
        lightToggle(light3,0)
        time.sleep(SleepTimeQ) 
        lightToggle(light4,0)
        time.sleep(SleepTimeQ) 
        lightToggle(light5,0)
        time.sleep(SleepTimeQ) 
        lightToggle(light6,0)
        time.sleep(SleepTimeQ) 
        

        lightToggle(light1,1)
        time.sleep(SleepTimeQ) 
        lightToggle(light2,1)
        time.sleep(SleepTimeQ) 
        lightToggle(light3,1)
        time.sleep(SleepTimeQ) 
        lightToggle(light4,1)
        time.sleep(SleepTimeQ) 
        lightToggle(light5,1)
        time.sleep(SleepTimeQ) 
        lightToggle(light6,1)
        time.sleep(SleepTimeQ) 



        lightToggle(light1,0)
        time.sleep(SleepTimeQ) 
        lightToggle(light2,0)
        time.sleep(SleepTimeQ) 
        lightToggle(light3,0)
        time.sleep(SleepTimeQ) 
        lightToggle(light4,0)
        time.sleep(SleepTimeQ) 
        lightToggle(light5,0)
        time.sleep(SleepTimeQ) 
        lightToggle(light6,0)
        time.sleep(SleepTimeQ) 

def closeP():
    '''at end of program - turn off all lights'''
    lightToggle(lightlist[0],0)
    lightToggle(lightlist[1],0)
    lightToggle(lightlist[2],0)
    lightToggle(lightlist[3],0)
    lightToggle(lightlist[4],0)
    lightToggle(lightlist[6],0)
    print("exit with no errors")
    
def altBlink(num):
    '''alternate between sets of lights'''
    light1=lightlist[0]
    light2=lightlist[1]
    light3=lightlist[2]
    light4=lightlist[3]
    light5=lightlist[4]
    light6=lightlist[5]
    for x in ("b"*num):
        SleepTimeA=SleepTimeS/SleepTimeA
        lightToggle(light1,0)
        lightToggle(light2,1)
        lightToggle(light3,0)
        lightToggle(light4,1)
        lightToggle(light5,0)
        lightToggle(light6,1)
        time.sleep(SleepTimeA) 
        
        lightToggle(light1,1)
        lightToggle(light2,0)
        lightToggle(light3,1)
        lightToggle(light4,0)
        lightToggle(light5,1)
        lightToggle(light6,0)
        time.sleep(SleepTimeA) 
        
        lightToggle(light1,0)
        lightToggle(light2,1)
        lightToggle(light3,0)
        lightToggle(light4,1)
        lightToggle(light5,0)
        lightToggle(light6,1)
        # turn off lights

def blink(num):
    light1=lightlist[0]
    light2=lightlist[1]
    light3=lightlist[2]
    light4=lightlist[3]
    light5=lightlist[4]
    light6=lightlist[5]
    for x in ("b"*num):
        SleepTimeA=SleepTimeS/SleepTime[2]
        lightToggle(light1,0)
        lightToggle(light2,0)
        lightToggle(light3,0)
        lightToggle(light4,0)
        lightToggle(light5,0)
        lightToggle(light6,0)
        time.sleep(SleepTimeA) 
        
        lightToggle(light1,1)
        lightToggle(light2,1)
        lightToggle(light3,1)
        lightToggle(light4,1)
        lightToggle(light5,1)
        lightToggle(light6,1)
        time.sleep(SleepTimeA) 
        
def gradBlink(num):
    '''turn on lights gradually one by one'''
    light1=3
    light2=4
    light3=5
    light4=6
    light5=7
    light6=8
    for x in ("b"*num):
        SleepTimeA=.25
        lightToggle(light1,0)
        lightToggle(light2,0)
        lightToggle(light3,0)
        lightToggle(light4,0)
        lightToggle(light5,0)
        lightToggle(light6,0)
        time.sleep(SleepTimeA) 
        
        lightToggle(light1,1)
        lightToggle(light2,0)
        lightToggle(light3,0)
        lightToggle(light4,0)
        lightToggle(light5,0)
        lightToggle(light6,0)
        time.sleep(SleepTimeA) 
        
        lightToggle(light1,1)
        lightToggle(light2,1)
        lightToggle(light3,0)
        lightToggle(light4,0)
        lightToggle(light5,0)
        lightToggle(light6,0)
        time.sleep(SleepTimeA) 
        
        lightToggle(light1,1)
        lightToggle(light2,1)
        lightToggle(light3,1)
        lightToggle(light4,0)
        lightToggle(light5,0)
        lightToggle(light6,0)
        time.sleep(SleepTimeA) 

        lightToggle(light1,1)
        lightToggle(light2,1)
        lightToggle(light3,1)
        lightToggle(light4,1)
        lightToggle(light5,0)
        lightToggle(light6,0)
        time.sleep(SleepTimeA) 
        

        lightToggle(light1,1)
        lightToggle(light2,1)
        lightToggle(light3,1)
        lightToggle(light4,1)
        lightToggle(light5,1)
        lightToggle(light6,0)
        time.sleep(SleepTimeA) 


        lightToggle(light1,1)
        lightToggle(light2,1)
        lightToggle(light3,1)
        lightToggle(light4,1)
        lightToggle(light5,1)
        lightToggle(light6,1)
        time.sleep(SleepTimeA) 

        lightToggle(light1,1)
        lightToggle(light2,1)
        lightToggle(light3,1)
        lightToggle(light4,1)
        lightToggle(light5,1)
        lightToggle(light6,0)
        time.sleep(SleepTimeA)         

        lightToggle(light1,1)
        lightToggle(light2,1)
        lightToggle(light3,1)
        lightToggle(light4,1)
        lightToggle(light5,0)
        lightToggle(light6,0)
        time.sleep(SleepTimeA) 

        lightToggle(light1,1)
        lightToggle(light2,1)
        lightToggle(light3,1)
        lightToggle(light4,0)
        lightToggle(light5,0)
        lightToggle(light6,0)
        time.sleep(SleepTimeA) 

        lightToggle(light1,1)
        lightToggle(light2,1)
        lightToggle(light3,0)
        lightToggle(light4,0)
        lightToggle(light5,0)
        lightToggle(light6,0)
        time.sleep(SleepTimeA) 

        lightToggle(light1,1)
        lightToggle(light2,0)
        lightToggle(light3,0)
        lightToggle(light4,0)
        lightToggle(light5,0)
        lightToggle(light6,0)
        time.sleep(SleepTimeA) 

        lightToggle(light1,0)
        lightToggle(light2,0)
        lightToggle(light3,0)
        lightToggle(light4,0)
        lightToggle(light5,0)
        lightToggle(light6,0)
        time.sleep(SleepTimeA)         

def gradbBlink(num):
    '''gradBlink but backwards'''
    light1=3
    light2=4
    light3=5
    light4=6
    light5=7
    light6=8
    for x in ("b"*num):
        SleepTimeA=.25
        lightToggle(light1,0)
        lightToggle(light2,0)
        lightToggle(light3,0)
        lightToggle(light4,0)
        lightToggle(light5,0)
        lightToggle(light6,0)
        time.sleep(SleepTimeA) 
        
        lightToggle(light1,0)
        lightToggle(light2,0)
        lightToggle(light3,0)
        lightToggle(light4,0)
        lightToggle(light5,0)
        lightToggle(light6,1)
        time.sleep(SleepTimeA) 
        
        lightToggle(light1,0)
        lightToggle(light2,0)
        lightToggle(light3,0)
        lightToggle(light4,0)
        lightToggle(light5,1)
        lightToggle(light6,1)
        time.sleep(SleepTimeA) 
        
        lightToggle(light1,0)
        lightToggle(light2,0)
        lightToggle(light3,0)
        lightToggle(light4,1)
        lightToggle(light5,1)
        lightToggle(light6,1)
        time.sleep(SleepTimeA) 

        lightToggle(light1,0)
        lightToggle(light2,0)
        lightToggle(light3,1)
        lightToggle(light4,1)
        lightToggle(light5,1)
        lightToggle(light6,1)
        time.sleep(SleepTimeA) 
        

        lightToggle(light1,0)
        lightToggle(light2,1)
        lightToggle(light3,1)
        lightToggle(light4,1)
        lightToggle(light5,1)
        lightToggle(light6,1)
        time.sleep(SleepTimeA) 

        lightToggle(light1,1)
        lightToggle(light2,1)
        lightToggle(light3,1)
        lightToggle(light4,1)
        lightToggle(light5,1)
        lightToggle(light6,1)
        time.sleep(SleepTimeA) 


        lightToggle(light1,0)
        lightToggle(light2,1)
        lightToggle(light3,1)
        lightToggle(light4,1)
        lightToggle(light5,1)
        lightToggle(light6,1)
        time.sleep(SleepTimeA) 

        lightToggle(light1,0)
        lightToggle(light2,0)
        lightToggle(light3,1)
        lightToggle(light4,1)
        lightToggle(light5,1)
        lightToggle(light6,1)
        time.sleep(SleepTimeA)         

        lightToggle(light1,0)
        lightToggle(light2,0)
        lightToggle(light3,0)
        lightToggle(light4,1)
        lightToggle(light5,1)
        lightToggle(light6,1)
        time.sleep(SleepTimeA) 

        lightToggle(light1,0)
        lightToggle(light2,0)
        lightToggle(light3,0)
        lightToggle(light4,0)
        lightToggle(light5,1)
        lightToggle(light6,1)
        time.sleep(SleepTimeA) 

        lightToggle(light1,0)
        lightToggle(light2,0)
        lightToggle(light3,0)
        lightToggle(light4,0)
        lightToggle(light5,0)
        lightToggle(light6,1)
