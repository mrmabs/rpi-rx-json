#!/usr/bin/python

import json, cgi, cgitb, os

form = cgi.FieldStorage()

cgi_json = form.getvalue('x')

print "Content-type:text/html\r\n\r\n"

form = json.loads(cgi_json)

if (form['freq']):
	freq_hz = int(float(str(float(form['freq'])))) # lots os simple filters to ensure we only get a number!
	print freq_hz
	if (freq_hz == 0):
		os.system("sudo /usr/local/bin/freq_pi -q")
	else:
		os.system("sudo /usr/local/bin/freq_pi -f %d" % (freq_hz))
	
else:
	print "No freq"
