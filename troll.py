import os
import re
import subprocess

#Dankness follows

command = ""

angerLevel = 0

#prompt
laptopName = raw_input('Please enter the laptop\'s name: ')
userName = raw_input('Please enter the user name: ')

#main loop
while True: 
	command = raw_input(laptopName +  ":" + os.getcwd().rsplit('/', 1)[1] + " " + userName + "$ ")
	print command
	root = "hello"
	if root == "ls":
		print "ls"
	elif root == "cd":
		print "cd"
	elif root == "mkdir":
		print "mkdir"
	elif root == "rm":
		print "rm"
	elif root == "pwd":
		print "pwd"
	elif root == "git":
		print "git"
	elif root == "help":
		print "help"
	else:
		try:
			cmd = subprocess.Popen(re.split(r'\s+', command), stdout=subprocess.PIPE)
			cmd_out = cmd.stdout.read()
			print cmd_out

		except OSError:
			print "-bash: "+ command + " : command not found"
	