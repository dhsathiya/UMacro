import os, subprocess, re, pyperclip
from evdev import InputDevice, categorize, ecodes

dev = InputDevice('/dev/input/event15')
dev.grab()

# function to copy the code
copy_array = [0] * 10
xsel_old_value = ""

def copy_one_to_zero(key):
	number_pressed = int(key[-1])

	print("Number Pressed: ", number_pressed)


def copy_one_to_zero1(key):
	#print("number 0 to 1 pressed: " + key + "last letter is" + key[-1])
	#print(globals()['copy_%s' % key[-1]])
	#dpyperclip.copy(globals()['copy_%s' % key[-1]])
	#globals()['copy_%s' % key[-1]] = os.popen('xsel').read()
	
	selected_text = os.popen('xsel')
	read_selected_text = selected_text.read()
	selected_text.close()

	if xsel_old_value == read_selected_text:
		return

	number_pressed=int(key[-1])
	if copy_array[number_pressed] != 0:
	  pyperclip.copy(copy_array[number_pressed])
	copy_array[number_pressed] = read_selected_text

	print("VALUE: " + copy_array[number_pressed])
	print("READ SELECTED TEXT: " + read_selected_text )
	print("NUMBER PRESSED: %d", number_pressed)
	print(*copy_array, sep = ", ")  
	print("########################################")

# Main loop
for event in dev.read_loop():

  if event.type == ecodes.EV_KEY:
	key = categorize(event)

	if key.keystate == key.key_down:
		#print(key.keycode)
		#print(os.popen('xsel').read())
		#subprocess.call(["/home/devarshi/macro.sh %s"%str(key.keycode)] , shell=True)
		m = re.search(r'KEY_\d$', key.keycode)

		if m is not None:
			copy_one_to_zero(key.keycode)

		if key.keycode == 'KEY_ESC':
			os.system('echo Hello World')
