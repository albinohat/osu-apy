## osu_player_stats.py
## Author: Daniel "Albinohat" Mercado
## 
## This script creates a text file containing some quick user statistics to display on a Twitch stream.

## TODO
## Add +/- updates for pp and rank.
##    Create + and - text files. Color the text accordingly in OBS.

## Standard Imports
import json, sys, time

## Third-party Imports
import osu_apy

if (len(sys.argv) != 4):
	print "    Invalid Syntax. Usage: osu_player_stats.py key_file output_file refresh\n" 
	print "    key_file    - A file containing your osu!api key."
	print "    output_file - A file in which to store the player stats."
	print "    refresh     - How often stats will be updated in seconds. (Minimum = 5)"
	sys.exit()

f = open(sys.argv[1], "r")
dev_key = f.read().strip()
f.close()

while(1):
	## Request player stats from the server.
	try:
		stats_json = json.loads(osu_apy.get_user(dev_key, "albinohat", "", "string", ""))

	except IOError:
		print "Unable to connect to osu!api. Will retry again in " + str(sys.argv[3]) + "seconds."
		
	## Open the file displayed on stream, write to it and close it.
	## Line 1 - Username
	## Line 2 - PP Rank
	## Line 3 - PP
	## Line 4 - Accuracy (Truncated to 2 decimal places.)	
	stats_file = open(sys.argv[2], "w+")
	stats_file.write(str(stats_json[0]["username"]).title() + "\n")
	stats_file.write("Rank:" + str(stats_json[0]["pp_rank"]) + "\n")
	stats_file.write("PP: " + str(stats_json[0]["pp_raw"]).split(".", 1)[0] + "\n")
	stats_file.write("Accuracy: " + str(stats_json[0]["accuracy"])[:5] + "%")
	stats_file.close()
	
	## Update once per minute.
	time.sleep(str(sys.argv[3]))