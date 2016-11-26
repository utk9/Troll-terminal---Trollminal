import os
import re
import subprocess
import time
import sys
import threading
from random import randint
import time

# Dankness follows

angerLevel = 0 # maxes out at 5

laptopName = "blah"#raw_input('Please enter the laptop\'s name: ')
userName =  "boo"#raw_input('Please enter the user name: ')

num_commands_in_intrl = 0

# clear the old input >:D
os.system('cls' if os.name == 'nt' else 'clear')

def run_bash(command):
	try:
		cmd = subprocess.Popen(re.split(r'\s+', command), stdout=subprocess.PIPE)
		cmd_out = cmd.stdout.read()
		print cmd_out

	except OSError:
		print "-bash: "+ command + " : command not found"


def talk(str):
  for c in str:
    sys.stdout.write(c)
    sys.stdout.flush()
    time.sleep(0.05)
  time.sleep(1)
  print ""

def increaseAnger(anger):
	global angerLevel
	angerLevel = angerLevel + anger
	if angerLevel > 5: angerLevel = 5

def regulateAnger():
  threading.Timer(60, regulateAnger).start()
  global angerLevel
  if angerLevel != 0: angerLevel-=1


def troll_ls():
	files =  os.listdir(os.getcwd())
	for file in files:
		shouldPrint = randint(0,9)
		if (shouldPrint > 2): print file,
	print ('\n')

def troll_rm(name):
	print "Not like this! Please don't kill me"
	shouldDelete = raw_input("Continue: ")
	if shouldDelete == "y": run_bash("rm -r " + name)

regulateAnger()

talk("hi im terminal :D")

#prompt
laptopName = raw_input('Please enter the laptop\'s name: ')
userName = raw_input('Please enter the user name: ')

intervalStart = time.time()

#main loop
while True:
	rest = ""
	command = raw_input(laptopName +  ":" + os.getcwd().rsplit('/', 1)[1] + " " + userName + "$ ")
	
	
	if time.time() - intervalStart > 10:
		intervalStart = time.time()
		num_commands_in_intrl = 0

	if (num_commands_in_intrl > 4):
		print "Too many commands"


	if " " in command: # find the first space
		root = command[0:command.index(" ")]
		rest = command[command.index(" "): len(command)]
	else:
		root = command
	if root == "ls":
		troll_ls()
	elif root == "cd":
		print "cd"
	elif root == "mkdir":
		troll_mkdir()
	elif root == "rm":
		troll_rm(rest)
	elif root == "pwd":
		print "pwd"
	elif root == "git":
		print "git"
	elif root == "help":
		print "help"
	else:
		run_bash(command)

	num_commands_in_intrl+=1
		
