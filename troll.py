import os

#Dankness follows

directory = os.getcwd().rsplit('/', 1)[1]
command = ""

laptopName = raw_input('Please enter the laptop\'s name: ')
userName = raw_input('Please enter the user name: ')

# directory

while True: 
	command = raw_input(laptopName +  ":" + directory + " " + userName + "$ ")
	print command