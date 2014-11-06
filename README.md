scripts
=======

Basic unix scripts

===========
Very useful and generic unix scripts that I love.

1: snscreen:
	OVERVIEW:
		- This is for screen users
		- snscreen uses human-friendly README file to automatically setup
		multiple screen windows for you with just one command
		- This is useful for automation test setups, developement setups etc
	FEATURES:
		- Automatically create multiple windows with specific names
		- Automatically executes different commands in specific windows
		- Cool status bar
		- Automatically setsup session name so you can resume easily
		- Generic README file so you can do whatever you want in your
		screen windows

2: psetup:
	OVERVIEW:
		- This uses snscreen to automatically look for devices and creates test environment
		- It uses format mentioned in README file in ~/.psetuprc to create actual README file
		that will be used by snscreen to create screen session
	FEATURES:
		- Configurable setup - you can say how your screen windows should look like
		- Sets upsessionname to your devices name, so you can resume using screen -x device_name if you wish to

3: shutils:
	OVERVIEW:
		- These are some of the utility functions used by my scripts
		- myshelllogging: Provides logging with different verbosity level
		- myhmap: Provides hash map implementation for key-value lookup
