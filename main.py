#!/usr/bin/env python3

import RPi.GPIO as GPIO
import weight

GPIO.setmode(GPIO.BCM)

if __name__ == "__main__":
	# setup for the sensors
	# initialize as (ADC channel, CS, clock, input to MCP, output from MCP
	leftCorner = weight.Weight(0)
	leftCorner.setup()

	while True:
		for i in range(5):
			fsr = leftCorner.readADC()
			leftCorner.addToList(fsr)
		med = leftCorner.findMedian()
		print("med:", med)	
		inp = input()
		leftCorner.clearList()
		if(inp == "0"):
			GPIO.cleanup()
			break
