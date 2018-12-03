#!/usr/bin/python
import RPi.GPIO as GPIO
import importlib, time
import light
importlib.import_module("light")

#set up pins
light1=light.Light(11)
light2=light.Light(12)
light3=light.Light(13)
light4=light.Light(15)
light5=light.Light(16)
light6=light.Light(18)
light7=light.Light(22)
light8=light.Light(7)
#set up pin array
lightTa=[light3,light4,light5,light6,light7,light8]
#create light show array object with correct GPIO out pins
lightShow1=light.LightShow(1,lightTa,[6,1,1,.5])

lightShow1.oboblink()
