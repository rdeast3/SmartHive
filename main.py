#!/usr/bin/env python
# File Name: main.py
# Author: Ronald East

import RPi.GPIO as GPIO
import weight
import temp_humid

GPIO.setmode(GPIO.BCM)

if __name__ == "__main__":
	# setup for the sensors
	# initialize as (ADC channel, CS, clock, input to MCP, output from MCP
	leftCorner = weight.Weight(0)
	leftCorner.setup()
	temperature = temp_humid.TempHumid()

	while True:
		temperature.read()
		print "Temp:", temperature.temp
		print "Humid:", temperature.humid
		for i in range(5):
			fsr = leftCorner.readADC()
			leftCorner.addToList(fsr)
		med = leftCorner.findMedian()
		print "med:", med	
		inp = raw_input()
		leftCorner.clearList()
		if(inp == "0"):
			GPIO.cleanup()
			break
