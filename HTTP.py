import serial
import urllib.request
import urllib.parse

ser = serial.Serial('COM2', 9600, timeout=1)
ser.flushInput()
while True:
    data = ser.readline()
    if (len(data)>0):
        strData = data.decode("utf-8")
        strData = strData.rstrip("\r\n")
        values = strData.split(",")

        if(len(values) == 2):
            print("Temperature: ",values[0])
            print("User: ",values[1])
            
            url = "      "
            strfield1 = "&field1=" + values[0] + "&field2=" + values[1]
            
            url = url + strfield1 
            print(url)
            
            f = urllib.request.urlopen(url)
            
            print(f.read().decode('utf-8'))
            
            
            
            
            
            
            