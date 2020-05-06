#! python3

import webbrowser, sys, pyperclip

if len(sys.argv) > 1:
	address = ' '.join(sys.argv[1:])
else:
	# get the address from clipboard
	address = pyperclip.paste()

webbrowser.open('https://www.google.com/maps/place/' + address)