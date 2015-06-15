import RPi.GPIO as GPIO

class Weight(object):
	def __init__(self, prtNum):
		self.prtNum = prtNum
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
		self.weightList.append(adcVal)	
