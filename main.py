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
		fsr =leftCorner.readADC()
		leftCorner.addToList(fsr)
	
		print("FSR:", fsr)
		print("list:", leftCorner.weightList)
		inp = input()
		if(inp == "0"):
			GPIO.cleanup()
			break
