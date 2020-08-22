import os
import subprocess
import re
import pyperclip
import keyboard
import evdev

from evdev import InputDevice, categorize, ecodes

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

# function to copy the code
copy_array = [0] * 10
xsel_old_value = "NULL"

def copy_one_to_zero(key):

	global xsel_old_value
	number_pressed = int(key[-1])
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


# Init input device
dev = InputDevice(list_input_devices_and_select())
dev.grab()

# Loop to catch key strokes
for event in dev.read_loop():

	if event.type == ecodes.EV_KEY:
		key = categorize(event)

		if key.keystate == key.key_down:
			print(key.keycode)
			#print(os.popen('xsel').read())
			#subprocess.call(["/home/devarshi/macro.sh %s"%str(key.keycode)] , shell=True)
			m = re.search(r'KEY_\d$', key.keycode)

			if m is not None:
				copy_one_to_zero(key.keycode)

			if key.keycode == 'KEY_GRAVE':
				keyboard.press_and_release('ctrl+v')
				os.system('echo Hello World')
