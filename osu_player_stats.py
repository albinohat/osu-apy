## osu_player_stats.py
## Author: Daniel "Albinohat" Mercado
## 
## This script creates a text file containing some quick user stats to display on a Twitch stream.

## Standard Imports
import json, sys, time

## Third-party Imports
import osu_apy

if (len(sys.argv) != 3):
	print "    Invalid Syntax. Usage: osu_player_stats.py key_file output_file" 
	print "key_file must contain your osu!api developer key."
	sys.exit()

f = open(sys.argv[1], "r")
dev_key = f.read().strip()
f.close()

while(1):
	## Request player stats from the server.
	stats_json = json.loads(osu_apy.get_user(dev_key, "albinohat", "", "string", ""))

	## Open the file displayed on stream, write to it and close it.
	stats_file = open(sys.argv[2], "w+")
	stats_file.write(str(stats_json[0]["username"]).title() + "\nPP: " + str(stats_json[0]["pp_raw"]).split(".", 1)[0] + "\nAccuracy: " + str(stats_json[0]["accuracy"])[:5] + "%")
	stats_file.close()
	
	## Update once per minute.
	time.sleep(60)