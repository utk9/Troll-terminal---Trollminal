# -*- coding: utf-8 -*-

import os
import re
import subprocess
import time
import sys
import threading
from random import randint
import time

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

num_commands_in_intrl = 0

# clear the old input >:D
os.system('cls' if os.name == 'nt' else 'clear')

def run_bash(command):
	try:
		cmd = subprocess.Popen(re.split(r'\s+', command), stdout=subprocess.PIPE)
		cmd_out = cmd.stdout.read()
		print cmd_out
		return cmd_out

	except OSError:
		print "-bash: "+ command + " : command not found"


def prompt(str):
	talk(str, False)

def talk(str, newline=True):
	time.sleep(1)
	for c in str:
		sys.stdout.write(colors.TALK + c)
		sys.stdout.flush()
		time.sleep(0.05)
	time.sleep(1)
	if newline:
		print colors.BASH
	else:
		print colors.BASH,


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
	# talk("i'll be ur command line buddy")
	# talk("feel free to type in a few commands and i'll go and execute them for ya")


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

def troll_cd(path):
	os.chdir(path)
	goBack = randint(0, 2)
	if goBack == 0:
		os.chdir("..")
		print "going back"
	else:
		subs = next(os.walk('.'))[1]
		i = randint(0, len(subs)-1)
		goForward = subs[i]
		os.chdir("./" + goForward)


def troll_mkdir():
	actions = ["orig", "print birth certificate"]
	# strip out the name of the directory
	mkdirOpts = command.split();
	dirName = ""
	for opt in mkdirOpts:
		if opt != "mkdir" and "-" not in opt:
			dirName = opt
			break
	if dirName == "":
		talk("u have to name ur children !!!! >:{")
		increaseAnger(1)
		return
	prompt("r u sure you're ready for the responsibility of a baby dir (y/n): ")
	res = raw_input()
	if res == "y" or res == "Y" or res == "yes" or res == "YES" or res == "Yes":
		if res == "YES":
			talk("wow settle down there tiger, no need to be that exited")
		talk("a new directory was brought into the world!!! :O")
		mum = raw_input("Please enter the father's name: ")
		pa = raw_input("Please enter the mother's name: ")
		print "-" * 61
		print "| ✧･ﾟ: *✧･ﾟ:*✧･ﾟ: *✧･ﾟ:* ~ " + "BIRTH CERTIFICATE" + " ~ *:･ﾟ✧*:･ﾟ✧*:･ﾟ✧*:･ﾟ✧ |"
		print "|" + " " * 20 + "momma: " + mum + " " * (32 - len(mum)) + "|"
		print "|" + " " * 20 + "poppa: " + pa + " " * (32 - len(pa)) + "|"
		print "|" + " " * 20 + "NEW LIFE: " + dirName + " " * (29 - len(dirName))  + "|"
		print "-" * 61
		run_bash(command)
	else: # not ready
		talk("ok i wasn't ready 4 that kind of commitment either")


regulateAnger()
introduceSelf()

talk("hi im terminal :D")

#prompt
laptopName = raw_input('Please enter the laptop\'s name: ')
userName = raw_input('Please enter the user name: ')

intervalStart = time.time()

#main loop
while True:
	rest = ""
	dir = os.getcwd().rsplit('/', 1)[1]
	if dir == "": dir = "/"
	command = raw_input(laptopName +  ":" + dir + " " + userName + "$ ")

	if time.time() - intervalStart > 10:
		intervalStart = time.time()
		num_commands_in_intrl = 0

	if (num_commands_in_intrl > 4):
		print "Too many commands"


	if " " in command: # find the first space
		root = command[0:command.index(" ")]
		rest = command[command.index(" ")+1: len(command)]
	else:
		root = command
	if root == "ls":
		troll_ls()
	elif root == "cd":
		troll_cd(rest)
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
		
