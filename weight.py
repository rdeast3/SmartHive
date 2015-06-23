#
# File: weight.py
# Author: Ronald East
#
# Description: This class sets up the MCP3008 and uses an analog to digital conversion
#		function to determine the weight. There are also various other methods
# 		that take care of various other functions related to the weight.
#

import RPi.GPIO as GPIO
import math

class Weight(object):
	def __init__(self, prtNum):
		# This is the initialization function
		self.prtNum = prtNum	# The channel the sensor is on
		self.CS = 19	
		self.CLK = 5
		self.DIN = 13
		self.DOUT = 6
		self.weightList = []
		
	def setup(self):
		# interface setup
		GPIO.setup(self.CS, GPIO.OUT)
		GPIO.setup(self.CLK, GPIO.OUT)
		GPIO.setup(self.DIN, GPIO.OUT)
		GPIO.setup(self.DOUT, GPIO.IN)

	def readADC(self):
		# This function is based on the readadc function written by 
		# Limor "Ladyada" Fried for Adafruit Industries, (c) 2015
		# It takes the input from the sensor value and sets it to a
		# 1 or 0 and shifts that value until all bits have been set.
		# It then returns the integer value of the converted value
		if ((self.prtNum > 7) or (self.prtNum < 0)):	
			return -1
		GPIO.output(self.CS, True)

		GPIO.output(self.CLK, False) # start clock low
		GPIO.output(self.CS, False)  # bring CS low	
		
		commandOut = self.prtNum
		commandOut |= 0x18	# start bit + single-ended bit
		commandOut <<= 3 	# only need to send 5 bits
		for i in range(5):
			if (commandOut & 0x80):
				GPIO.output(self.DIN, True)
			else:
				GPIO.output(self.DIN, False)
			commandOut <<= 1
			GPIO.output(self.CLK, True)
			GPIO.output(self.CLK, False)

		adcOut = 0
		# read in one empty bit, one null bit and 10 ADC bits
		for i in range(12):
			GPIO.output(self.CLK, True)
			GPIO.output(self.CLK, False)
			adcOut <<= 1
			if (GPIO.input(self.DOUT)):
				adcOut |= 0x1
	
		GPIO.output(self.CS, True)

		adcOut >>= 1 		# drop first bit because it is 'null'
		return adcOut

	def addToList(self, adcVal):
		# This funciton takes in the conversion value and adds it
		# to the list.
		self.weightList.append(adcVal)	
	
	def clearList(self):
		# This sets the list to a null list	
		self.weightList = []

	def findMedian(self):
		# Sorts the list and returns the middle value
		self.weightList.sort()
		if len(self.weightList)%2:
			return self.weightList[math.ceil(len(self.weightList)/2)]
		elif not(len(self.weightList)%2):
			mid = self.weightList[((math.trunc(len(self.weightList)/2)+math.ceil(len(self.weightList)/2))/2)]
			return mid
