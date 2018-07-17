import serial
import numpy
import requests

arduinoSerialData = serial.Serial('/dev/ttyUSB0',9600)
myData = []

while True:
    if(arduinoSerialData.inWaiting()>0):
        myData.append((int(arduinoSerialData.readline())))
        
        if len(myData) == 4:
            average = numpy.mean(myData)
            print average
            r = requests.post('https://healthsystem.ddns.net/hs/raspberry/eballintime0', json = {'BPM': average, 'pwd':'tecweb' })
            myData = []
