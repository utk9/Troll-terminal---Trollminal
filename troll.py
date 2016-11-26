import os
import re
import subprocess
import time
import sys
import threading
from random import randint

# Dankness follows

class colors:
	TALK = "\033[35m"
	BASH = "\033[0m"

ASCII_COMPUTER = """
 ._________________.
 | _______________ |
 | I             I |
 | I   O     O   I |
 | I      -      I |
 | I    \___/    I |
 | I_____________I |
 !_________________!
    ._[_______]_.
.___|___________|___.

"""

angerLevel = 0 # maxes out at 5
laptopName = "blah"#raw_input('Please enter the laptop\'s name: ')
userName =  "boo"#raw_input('Please enter the user name: ')

# clear the old input >:D
os.system('cls' if os.name == 'nt' else 'clear')

def run_bash(command):
	try:
		cmd = subprocess.Popen(re.split(r'\s+', command), stdout=subprocess.PIPE)
		cmd_out = cmd.stdout.read()
		print cmd_out

	except OSError:
		print "-bash: "+ command + " : command not found"
		talk("do u know what ur doing")


def talk(str):
	time.sleep(1)
	for c in str:
		sys.stdout.write(colors.TALK + c)
		sys.stdout.flush()
		time.sleep(0.05)
	time.sleep(1)
	print colors.BASH

def increaseAnger(anger):
	global angerLevel
	angerLevel = angerLevel + anger
	if angerLevel > 5: angerLevel = 5

def regulateAnger():
	threading.Timer(60, regulateAnger).start()
	global angerLevel
	if angerLevel != 0: angerLevel-=1

def introduceSelf():
	print colors.TALK + ASCII_COMPUTER
	talk("hi im terminal :D")
	talk("i'll be ur command line buddy")
	talk("feel free to type in a few commands and i'll go and execute them for ya")

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
introduceSelf()

#prompt
laptopName = raw_input('Please enter the laptop\'s name: ')
userName = raw_input('Please enter the user name: ')

#main loop
while True:
	rest = ""
	command = raw_input(laptopName +  ":" + os.getcwd().rsplit('/', 1)[1] + " " + userName + "$ ")
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
