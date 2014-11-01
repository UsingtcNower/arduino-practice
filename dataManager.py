import serial
import re
import MySQLdb
import time

ser = serial.Serial('/dev/ttyACM0', 9600, timeout=2)
db = MySQLdb.connect(host='localhost', user='user', passwd='passwd', db='monitor')
regx = re.compile(r'Humidity\s*=\s*(\d+)')
line = ser.readline()
while line :
	match = regx.search(line)
	if(match):
		value = match.group(1)
		cursor = db.cursor()
		cmd = "INSERT INTO humidity(time_id,humidity_value) VALUES({0}, {1})".format(time.time(), value)
		cursor.execute(cmd)
		db.commit()
		#print cmd
	line = ser.readline()
db.close()
