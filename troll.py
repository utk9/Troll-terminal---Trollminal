import os
import re
import subprocess
import time
import sys

# Dankness follows

angerLevel = 0 # maxes out at 5

laptopName = "blah"#raw_input('Please enter the laptop\'s name: ')
userName =  "boo"#raw_input('Please enter the user name: ')

# clear the old input >:D
os.system('cls' if os.name == 'nt' else 'clear')

#prompt
laptopName = raw_input('Please enter the laptop\'s name: ')
userName = raw_input('Please enter the user name: ')

def talk(str):
  for c in str:
    sys.stdout.write(c)
    sys.stdout.flush()
    time.sleep(0.05)
  time.sleep(1)
  print ""

talk("hi im terminal :D")

#main loop
while True:
	command = raw_input(laptopName +  ":" + os.getcwd().rsplit('/', 1)[1] + " " + userName + "$ ")
	if " " in command: # find the first space
		root = command[0:command.index(" ")]
	else:
		root = command
	print command
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
