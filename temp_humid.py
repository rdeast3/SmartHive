# File name: temp_humid.py
# Author: Ronald East
# Description: This file contains the class for the temperature and humidity sensor.
#		It contains the initialization of the sensor and all helper functions
#		needed to read the temperature and humidity.
	# add more as file written

# Copyright for the functions under the Adafruit_DHT module is as follows
# 	Copyright (c) 2014 Adafruit Industries
#	Author: Tony DiCola
#
#	Permission is herby granted, free of charge, to andy person obtaining a
# copy of this software and associated documentation files (the "Software"), to 
# deal in the Software without restriction, including without limitation the 
# rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
# sell copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all 
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EBENT SHALL THE 
# AUTHOS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import RPi.GPIO as GPIO
import Adafruit_DHT

class TempHumid(object):
	def __init__(self):
		self.type = Adafruit_DHT.DHT11
		self.pin = 21
		self.temp = 0 
		self.humid = 0

	def read(self):
		humidRead, tempRead = Adafruit_DHT.read_retry(self.type, self.pin)
		self.temp = tempRead
		self.humid = humidRead
