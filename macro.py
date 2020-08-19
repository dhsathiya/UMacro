import os, subprocess, re
from evdev import InputDevice, categorize, ecodes

dev = InputDevice('/dev/input/event15')
dev.grab()

# function to copy the code
def copy_one_to_zero(key):
	print("number 0 to 1 pressed: " + key)

# Main loop
for event in dev.read_loop():

  if event.type == ecodes.EV_KEY:
	key = categorize(event)

	if key.keystate == key.key_down:
		#print(key.keycode)
		#print(os.popen('xsel').read())
		subprocess.call(["/home/devarshi/macro.sh %s"%str(key.keycode)] , shell=True)
		m = re.search(r'KEY_\d$', key.keycode)

		if m is not None:
			copy_one_to_zero(key.keycode)

		if key.keycode == 'KEY_ESC':
			os.system('echo Hello World')
