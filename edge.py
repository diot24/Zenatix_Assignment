# You have to write a forever executable python program to read sensor data and send it to the cloud server.

import serial
import time
import csv

# set up the serial line
ser = serial.Serial('COM4', 9600)
time.sleep(2)

# Read and record the data
data =[]                       # empty list to store the data
for i in range(50):
	b = ser.readline()         # read a byte string
        string_n = b.decode()  # decode byte string into Unicode  
	string = string_n.rstrip() # remove \n and \r
	print(string)
	data.append(string)           # add to the end of data list
	time.sleep(60)            # wait (sleep) 0.1 seconds

ser.close()

# Open and save data to csv file
with open('sensor_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Timestamp", "Value", "Sensor"])
    timestamp = message['timestamp']
    value   = message['vaue']
    sensor  = message['sensor']
    with open('results.csv', 'a+') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([timestamp, value, sensor])
    
