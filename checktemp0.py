
import serial
import time
# set up the serial line
ser = serial.Serial('/dev/cu.wchusbserialfd120', 9600)
time.sleep(2)

# Read and record the data

for i in range(1):
    b = ser.readline()         # read a byte string
    string_n = b.decode()  # decode byte string into Unicode
    string = string_n.rstrip() # remove \n and \r
    temperature = float(string)        # convert string to float
    time.sleep(0.1)            # wait (sleep) 0.1 seconds

ser.close()
# show the data