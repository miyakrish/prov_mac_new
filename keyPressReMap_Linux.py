import sys
import subprocess
#import pdb

#pdb.set_trace()
remap_command = 'xmodmap -e "keycode %s = space"'
restore_command = "setxkbmap -layout us"

# Add new keycodes to remap here in this array
keycodes_to_remap = [37, 64, 108, 9, 205,105, 37,218,107, 50, 160 ]

if "remap" in sys.argv:
	for keycode in keycodes_to_remap:
	    subprocess.Popen(remap_command % keycode, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
elif "reset" in sys.argv:
	subprocess.Popen(restore_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
else:
        print ("Please provide a proper command to remap")
