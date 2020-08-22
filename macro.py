import os
import subprocess
import re
import pyperclip
import keyboard
import evdev
import sys
import importlib
import yaml
from dmacro_conf import *
from evdev import InputDevice, categorize, ecodes

# Import dmacro_conf 
#import_file_name = sys.argv[1]


# Event key pressed value
# key_pressed = key.keycode
key_pressed = "NULL"

# Sub command of
config_command_to_execute = "NULL"

# clip board array of size 10.
# can store 10 clips
copy_array = [0] * 10

# value of last clip to stop overriding
xsel_old_value = "NULL"

# Class for text colors
class bcolors:
	HEADER = '\033[95m'
	OKBLUE = '\033[34m'
	OKGREEN = '\033[32m'
	OKYELLOW = '\033[33m'
	WARNING = '\033[93m'
	FAIL = '\033[31m'
	ENDC = '\033[0m'
	BOLD = '\033[1m'
	UNDERLINE = '\033[4m'

# ---------------------
# INITIAL PART
# ---------------------
# input device list
def list_input_devices_and_select():

	devices = [evdev.InputDevice(path) for path in evdev.list_devices()]
	list_item=0
	devices.reverse()
	for device in devices:
		print( bcolors.OKBLUE ,list_item, ") ", bcolors.ENDC, bcolors.OKYELLOW,device.path, device.name, device.phys, bcolors.ENDC)
		list_item+=1

	user_selected_input_device_number = int(input("Enter device number to use as macro:"))
	if user_selected_input_device_number > list_item or user_selected_input_device_number < 0:
		print(bcolors.FAIL, "Please select an appropriate number", bcolors.ENDC)
		exit()
	
	return devices[user_selected_input_device_number].path

# ---------------------
# DMACRO FEATURES
# ---------------------
# function to copy
def copy_to_clipboard():
	global key_pressed
	key_pressed = key.keycode
	global xsel_old_value
	number_pressed = int(key_pressed[-1])
	xsel_current_value = os.popen('xsel').read()

	if xsel_current_value != xsel_old_value:
		xsel_old_value = xsel_current_value
		copy_array[number_pressed] = xsel_current_value
	
	pyperclip.copy(copy_array[number_pressed])

	print("Number Pressed:        ", number_pressed)
	print("xsel_current_value:    ", xsel_current_value)
	print("Current value to copy: ", copy_array[number_pressed])
	print(*copy_array, sep = ", ")
	print("-------------------------------------")

# function to paste
# ctrl + v
def paste():
	keyboard.press_and_release('ctrl+v')

# terminal paste
def term_paste():
	keyboard.press_and_release('ctrl+shift+v')

def execute(cmd):
	subprocess.call(["xdotool", "type", cmd])
	keyboard.press_and_release('enter')

# function to execute shell script
def execute_shell(cmd):
	subprocess.Popen(cmd, shell=True, executable='/bin/bash')

# ---------------------
# MAIN FUNCTION 
# ---------------------
# Init input device
dev = InputDevice(list_input_devices_and_select())
dev.grab()

# Loop to catch key strokes
for event in dev.read_loop():

	if event.type == ecodes.EV_KEY:
		key = categorize(event)

		if key.keystate == key.key_down:
			print(key.keycode)
			
			key_pressed_config_value = eval(key.keycode)

			config_command = key_pressed_config_value.split(' ', 1)[0] 
			function_name_call = config_command + '()'
			
			if config_command == 'execute_shell':
				config_command_to_execute = key_pressed_config_value.split(' ', 1)[1]
				function_name_call = config_command + '(' + config_command_to_execute + ')'
				#print("REACHED EXECUTE")
				#print(config_command)
				#print(config_command_to_execute)
			
			if config_command == 'execute':
				config_command_to_execute = key_pressed_config_value.split(' ', 1)[1]
				function_name_call = config_command + '(' + config_command_to_execute + ')'

			#eval(function_name)
			try:
			    eval(function_name_call)
			except NameError:
			    print("Not in scope!")
			else:
			    print("In scope!")


			'''
			#eval( key_pressed + '(' + key.keycode + ')')
			#print(os.popen('xsel').read())
			#subprocess.call(["/home/devarshi/macro.sh %s"%str(key.keycode)] , shell=True)

			m = re.search(r'KEY_\d$', key.keycode)

			if m is not None:
				copy_one_to_zero(key.keycode)

			if key.keycode == 'KEY_GRAVE':
				keyboard.press_and_release('ctrl+v')
				os.system('echo Hello World')
			'''
