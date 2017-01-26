#!/usr/bin/python

import json, cgi, cgitb

form = cgi.FieldStorage()

json = form.getvalue('x')

print "Content-type:text/html\r\n\r\n"

print json
