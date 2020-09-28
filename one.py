#!/usr/bin/python3

print("content-type:text/html")
print()

import cgi
import subprocess as sp 


a=["Rahul"]
b=["lucky@1"]

form=cgi.FieldStorage()
user=form.getvalue('user')
passwd=form.getvalue('passwd')
if(user in a):
	if(passwd in b):
		final=sp.getoutput("cat /var/www/html/command.html")
	else:
		print("Invalid password")
else:
	print("Invalid username")

print(final)

