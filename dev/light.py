#!/usr/bin/python
import RPi.GPIO as GPIO
import time

class Light:  
    '''light object'''
    def __init__(self, pin, name, state = False):
        self.pin=pin
        self.state=state
        self.name=name
    
	def setState(self, state = False):
		self.state = state
		GPIO.output(self.pin, state)
		print("Light " + self.name + " is now " + self.state == True and "ON" or "OFF")
	
    def toggle(self):
		self.setState(not self.state)

# A basic rewrite of LightShow.
class LightShow(Light):
	def __init__(self, Delay, Lights, TimeFactors):
		self.Lights = Lights           # Array of lights
		self.Delay = Delay             # Delay of lights
		self.TimeFactors = TimeFactors # Time Factors
		self.CurrentTimeFactor = 0     # Index of the current time factor
	
	def setStateOfLight(self, index = 0, state = False): # Sets the state of a single light.
		self.Lights[index].setState(state)
		
	def getLight(self, index = 0): # Gets a light at the specified index.
		return self.Lights[index]
	
	def setStateOfLights(self, state = False): # Sets the state of all lights.
		for i in range(len(self.Lights)):
			self.setStateOfLight(i, state)
	
	# Convenience functions to turn off/on lights.
	def turnOffLights(self): self.setStateOfLights()
	def turnOnLights(self): self.setStateOfLights(True)
	def toggleLights(self): 
		for i in range(len(self.Lights)):
			self.getLight(i).setState(not self.getLight(i).state) # (not self.getLight(i).state)
	
	def sleepFactor(self): # Sleeps for the light show's current time factor.
		time.sleep(self.Delay * self.TimeFactors[self.CurrentTimeFactor])
	
	# Light show functions
	def blink(self, times = 1):
		self.CurrentTimeFactor = 0
		for i in range(times):
			self.turnOnLights()  # Turns on the lights
			self.sleepFactor()   # Waits a little
			self.turnOffLights() # Turns off the lights
			self.sleepFactor()   # Waits a little
		
	def onebyone_blink(self, times = 1, doBackwards = False): # One By One Blink, support for backwards
		self.turnOffLights()                             # Turns off the lights
		self.CurrentTimeFactor = 1                       # Changes the index of the time factor
		
		for i in range(times):
			if doBackwards == True:
				for i in range(len(self.Lights) - 1, 0, -1): # Goes down through the list of lights and toggles them
					self.getLight(i).toggle()
					self.sleepFactor()
					
				for i in range(len(self.Lights)):            # Goes up the list of lights and toggles them again
					self.getLight(i).toggle()
					self.sleepFactor()
			else:
				for i in range(len(self.Lights)):            # Goes up through the list of lights and toggles them
					self.getLight(i).toggle()
					self.sleepFactor()
				
				for i in range(len(self.Lights), 0, -1):     # Goes down the list of lights and toggles them again
					self.getLight(i).toggle()
					self.sleepFactor()
		
		self.turnOffLights() # Turns off the lights.
	
	def bounce(self, times = 1): # Bounces the lights.
		self.turnOffLights()       # Turns off the lights
		self.CurrentTimeFactor = 1 # Changes the index of the time factor.
		
		for i in range(times):
			for i in range(len(self.Lights)):        # Goes up through the list of lights and blinks it.
				self.getLight(i).toggle()
				self.sleepFactor()
				self.getLight(i).toggle()
				
			for i in range(len(self.Lights), 0, -1): # Goes down the list of lights and toggles them again.
				self.getLight(i).toggle()
				self.sleepFactor()
				self.getLight(i).toggle()
		self.turnOffLights() # Turns off the lights
	
	def row_blink(self, times = 1):
		self.turnOffLights()           # Turns off the lights 
		self.CurrentTimeFactor = 2     # Changes the index of the time factor.
		for i in range(times):
			self.turnOnLights()        # Turns on the lights
			self.sleepFactor()         # Sleeps for amount of time in the array of time factors
			self.turnOffLights()       # Turns off the lights
			self.sleepFactor()         # Sleeps for amount of time in the array of time factors
	
	def gc_blink(self):
		self.turnOffLights()
		self.CurrentTimeFactor = 1
		self.getLight(0).setState(True) # G and C
		self.sleepFactor()
		self.getLight(1).setState(True)
		self.sleepFactor()
		self.CurrentTimeFactor = 3      # H and S
		self.getLight(2).setState(True)
		self.sleepFactor()
		self.getLight(3).setState(True)
		self.sleepFactor()
		self.turnOffLights()            # Turns off all lights at the end.
	
	def alternative_blink(self, times = 1)
		times = times * 2
		self.CurrentTimeFactor = 3 # Changes the index of the time factor
		
		for i in range(times):
			for i,v in enumerate(self.Lights): # Goes through the array of lights with the enumerate function.
				if i%2==0:                     # If index is even
					v.setState(True)           # Turns the light on
				else:                          # Else
					v.setState(False)          # Turns the light off
			self.sleepFactor()                 # Sleeps for amount of time in the array of time factors
			
			for i in range(self(len.Lights)):
				self.getLight(i).toggle()
			self.sleepFactor()
		self.turnOffLights()