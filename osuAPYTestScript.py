## osuAPYTestScript
## Author: Daniel "Albinohat" Mercado
##
## Test script for the osuAPY module.

## Standard imports
import sys

## Third-party imports
import osuAPY

if (len(sys.argv) != 2):
	print "    Invalid Syntax. Usage: osuAPY.py key_file. key_file must contain your osu!api developer key."
	sys.exit()

f = open(sys.argv[1])

dev_key = f.read().strip()

print dev_key