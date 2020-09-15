# UMacro ![Generic badge](https://img.shields.io/badge/Status-Beta-Yellow.svg) ![Open Source Love svg2](https://badges.frapsoft.com/os/v2/open-source.svg?v=103)

[![License](https://img.shields.io/badge/License-MIT-success.svg)](https://opensource.org/licenses/MIT)
![Made With Python](https://img.shields.io/badge/Made%20With-Python-blue)
![Tested On Ubuntu 20.04](https://img.shields.io/badge/Tested%20On-Ubuntu%2020.04-orange)

> No need to grow plants in old keyboards anymore.

UMacro is cli tool to use a keyboard as macro keyboard.

## Functions
1. Execute script
2. Execute a single command
3. Type string
4. Send keystroke
5. Copy to clipboard (selected text)
6. Paste
7. Terminal paste

## Commands

### Installation
```shell
wget -q -O - https://raw.githubusercontent.com/dhsathiya/umacro/master/setup.sh | sudo bash
```

### Running
1. Run following command:
	```shell
	sudo umacro
	```
2. Select the device from the list.

### Termination
```shell
sudo umacro terminate
```

### Check key code
```shell
sudo umacro check-key
```

## Configuration
Configuration file: `/etc/umacro/umacro_conf.yml`

[Example Configuration](umacro_conf.yml)

### Syntax:
```yaml
KEY_CODE: "FUNCTION 'ARGUMENT'"
``` 

#### Functions:
1. execute_shell
	- Executes a bash script.

2. execute
	- Executes a command.

3. typeto
	- Types string.

4. keystroke
	- Sends keystroke.
	- Multiple keys can be combined with `+`.

5. copy_to_clipboard
	- Store the selected element to a hotkey. Which later can be used by clicking the hotkey again and then paste.
	- Currently only supports standard numeric keys(top 1-0 keys).

6. paste
	- Simple paste: <kbd>ctrl</kbd> + <kbd>v</kbd>

7. term_paste
	- Paste for terminal: <kbd>ctrl</kbd> + <kbd>shift</kbd> + <kbd>v</kbd>

## Dependency
[xdotool](http://manpages.ubuntu.com/manpages/trusty/man1/xdotool.1.html) for better support on special characters. Also works without it.

## ToDo
1. Fix dirty code.
2. Multiple keyboard/input-device support.
3. Add keyboard modes.
4. Multi-key shortcut support.
There's a long list...
