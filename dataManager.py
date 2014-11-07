import serial
import re
import MySQLdb
import time

ser = serial.Serial('/dev/ttyACM0', 9600, timeout=2)
db = MySQLdb.connect(host='localhost', user='root', passwd='653800', db='monitor')
regx = r'(Humidity|Temperature) = (\d+)'
line = ser.readline()
while line :
	#print line
	match = re.findall(regx, line)
	if(match):
		#print match
		time_id = time.time()
		humidity = match[0][1]
		cursor = db.cursor()
		cmd = "INSERT INTO humidity(time_id,humidity_value) VALUES({0}, {1})".format(time_id, humidity)
		#print cmd
		cursor.execute(cmd)
		db.commit()
		temperature = match[1][1]
		cursor = db.cursor()
		cmd = "INSERT INTO temperature(time_id,temperature_value) VALUES({0}, {1})".format(time_id, temperature)
		cursor.execute(cmd)
		#print cmd
		db.commit()
		#print cmd
	line = ser.readline()
db.close()
