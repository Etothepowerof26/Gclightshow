import RPi.GPIO as GPIO
import time
class Light:  
    '''light object'''
    def __init__(self, pin,state=False):
        self.pin=pin
        self.state=state

    def getState(self):
        return self.state
    
    def toggle(self):
        if(self.state):
            #light on
            GPIO.output(self.pin, False)
        elif(not self.state):
            GPIO.output(self.pin, True)
    
    def allOff(self):
        GPIO.output(self.pin, False)

class LightShow(Light):
    '''List of lights and their respective functions
        initialized variables in list of:
        standard time, array of light objects, array of time factors
        
        array of times should be in this order:
        blink,
    '''
    def __init__(self, standardTimeS, lightL, timeA):
        #array of lights
        self.lightL=lightL
        #standard time for light on
        self.standardTimeS=standardTimeS
        #array of time factors
        self.timeA=timeA
        #number of lights
        self.countT=len(lightL)

    def offP(self):
        for x in self.lightL:
            self.lightL[x].allOff()  
    def blink(self, times):
        #get rid of this to optimize
        self.offP()

        #turn lights on
        for x in self.lightL:
            self.lightL[x].toggle()
        time.sleep(self.standardTimeS*self.timeA[0])
        for x in self.lightL:
            self.lightL[x].toggle()
        #turn lights off

        #get rid of this to optimize
        self.offP()
    def oboblink(self):
        '''One by one blink'''
        self.offP()
        #number of times it'll take to blink up and down
        #self.countT=self.countT*2+1
        # old code btw
        #populate light state array with falses
        #lightS=[]
        # for x in self.lightL:
        #     lightS.append(False)

        for x in range(0,len(self.lightL)):
            self.lightL[x].toggle()
            time.sleep(self.standardTimeS*self.timeA[1])
        #bootleg way to turn them off then that way
        #i found a better way but I like it bootleg
        #maybe i'll optimize it later
        count1=self.countT-1
        count2=0
        while (count1-count2)>=0:
            self.lightL[count1-count2].toggle()
            count2+=1
            time.sleep(self.standardTimeS*self.timeA[2])
        self.offP()

    def obobblink(self):
        '''One by one blink backwards'''
        self.offP()
        for x in range(-len(self.lightL)+1,1):
            self.lightL[-x].toggle()
            time.sleep(self.standardTimeS*self.timeA[1])
        for x in range(0,len(self.lightL)):
            self.lightL[x].toggle()
            time.sleep(self.standardTimeS*self.timeA[1])
        self.offP()