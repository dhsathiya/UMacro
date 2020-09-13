# dmacro ![Generic badge](https://img.shields.io/badge/Status-Beta-Yellow.svg) ![Open Source Love svg2](https://badges.frapsoft.com/os/v2/open-source.svg?v=103)

An excellent way to use you old keyboard.

DMacro can convert your old keyboard in an macro keyboard.

**From**
<img src="https://i.pinimg.com/originals/9c/bc/e5/9cbce515b136029d504e3bbf048639a9.jpg" alt="Keyboard with Plants" width="200"/>
**To**
<img src="https://i.redd.it/uc8a2awui0uz.png" alt="Multiple Macro Keyboards" width="200"/>

_source:reddit_

_source:www.pinterest.ca_


## Installation

```bash
wget
```

## Configuration file
`$HOME/.dmacrorc`

### Syntax
```yaml
<KEY_CODE>: "<COMMAND> '<ARGUMENT>'"
```

#### Commands
**copy_to_clipboard**

Copy the current selection to the numerical key.

Applicable to only top Numeric keys only.

<kbd>1</kbd>, <kbd>2</kbd>, <kbd>3</kbd>, <kbd>4</kbd>, <kbd>5</kbd>, <kbd>6</kbd>, <kbd>7</kbd>, <kbd>8</kbd>, <kbd>9</kbd>, <kbd>0</kbd>

Example:
```yaml
KEY_1: "copy_to_clipboard"
```

**paste**

Send keystroke: <kbd>ctrl</kbd> + <kbd>v</kbd>

**term_paste**

Send keystroke: <kbd>ctrl</kbd> + <kbd>shift</kbd> + <kbd>v</kbd>

**execute_shell**

Execute shell script

Example:
```yaml
KEY_S: "execute_shell '/home/example/dmacro/example.sh'"
```

**execute**

Execute a command in terminal.

Example:
```yaml
KEY_L: "execute 'ls -al'"
```

**type**

Type a string where the cursor is.

Example:
```yaml
KEY_T: "type 'df -h /'"
```

## Todo

- Programmatic improvements
- Fix dirty code
- Proper way to close the program
