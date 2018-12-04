#!/usr/bin/python
import RPi.GPIO as GPIO
import time

class Light:  
    '''light object'''
    def __init__(self, pin,name,state=False):
        self.pin=pin
        self.state=state
        self.name=name

    def getState(self):
        return self.state
    
    def toggle(self):
        #if on then off
        if(self.state==True):
            #light off
            GPIO.output(self.pin, False)
            self.state=False
            print("light "+ self.name+" off")
        elif(self.state==False):
            GPIO.output(self.pin, True)
            print("light "+ self.name+" on")
            self.state=True
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

        #variables for alt blink
        self.lightB=False
        self.lighte=[]
        self.lighto=[]
    
    def altBlinkinit(self):
        for x in range(0,len(self.lightL)):
            if (x%2)==0:
                self.lighte.append(x)
            else:
                self.lighto.append(x)

    def offP(self):
        '''used to make sure all functions start at the same point every time'''
        for x in range(0,len(self.lightL)):
            self.lightL[x].allOff()  
    def blink(self, times):
        #get rid of this to optimize
        self.offP()

        #turn lights on
        for x in range(0,len(self.lightL)):
            self.lightL[x].toggle()
        time.sleep(self.standardTimeS*self.timeA[0])
        for x in range(0,len(self.lightL)):
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
            time.sleep(self.standardTimeS*self.timeA[1])
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
    
    def bounce(self):
        '''Bounce the light that is on from one end to another'''
        self.offP()
        for x in range(0,len(self.lightL)):
            self.lightL[x].toggle()
            time.sleep(self.standardTimeS*self.timeA[1])
            self.lightL[x].toggle()
        #leaves last light on
        for x in range(-len(self.lightL)+1,1):
            self.lightL[-x].toggle()
            time.sleep(self.standardTimeS*self.timeA[1])
            self.lightL[-x].toggle()
        self.offP()
    
    def rowblink(self):
        '''Turn on rows at a time'''
        self.offP()
        #turn all on
        for x in range(0,len(self.lightL)):
            self.lightL[x].toggle()
        #wait sleep time
        time.sleep(self.standardTimeS/self.timeA[2])
        #turn all off
        for x in range(0,len(self.lightL)):
            self.lightL[x].toggle()
        self.offP()
    
    def altBlink(self,num):
        '''blink lights based on array value (odd or even)'''
        self.offP()
        if not self.lightB:
            self.altBlinkinit()
        for x in range(0,num+1):
            for x in range(0,len(self.lighte)):
                #toggle even on
                #light_object_array[even array[iterator]].toggle()
                self.lightL[self.lighte[x]].toggle()
            time.sleep(self.standardTimeS/self.timeA[3])
            for x in range(0,len(self.lighte)):
                #toggle even off
                #light_object_array[even array[iterator]].toggle()
                self.lightL[self.lighte[x]].toggle()
            for x in range(0,len(self.lighto)):
                #toggle odd on
                self.lightL[self.lighto[x]].toggle()
            time.sleep(self.standardTimeS/self.timeA[3])
            self.offP()
    