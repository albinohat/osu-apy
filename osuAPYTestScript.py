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

print "Starting osuAPY Unit Tests"

print "\n=SET 1==================================================================="
print "osuAPY.get_beatmaps Method."

print "\n==TEST 1=="
print "Retrieving Beatmap info with since.\n"

print osuAPY.get_beatmaps(dev_key, "2014-12-18 12:00:00", "", "", "")

print "\n==TEST 2=="
print "Retrieving Beatmap info by beatmap set ID.\n"

print osuAPY.get_beatmaps(dev_key, "", "95647", "", "")

print "\n==TEST 3=="
print "Retrieving Beatmap info by beatmap ID.\n"

print osuAPY.get_beatmaps(dev_key, "", "", "256754", "")

print "\n==TEST 4=="
print "Retrieving Beatmap info by user ID. (Used a song I played to get back relevant info.)\n"

print osuAPY.get_beatmaps(dev_key, "", "", "256754", "2770894")

print "\n=SET 2==================================================================="
print "osuAPY.get_user Method."

print "\n==TEST 1=="
print "Retrieving user using defaults.\n"

print osuAPY.get_user(dev_key, "2770894", "", "", "")

print "\n==TEST 2=="
print "Retrieving user by mode.\n"

print osuAPY.get_user(dev_key, "2770894", "0", "", "")

print "\n==TEST 3=="
print "Retrieving user by user type (id).\n"

print osuAPY.get_user(dev_key, "2770894", "", "id", "")

print "\n==TEST 4=="
print "Retrieving user by user type (string).\n"

print osuAPY.get_user(dev_key, "albinohat", "", "string", "")

print "\n==TEST 5=="
print "Retrieving user by event days.\n"

print osuAPY.get_user(dev_key, "2770894", "", "", "31")

print "\n=SET 3==================================================================="
print "osuAPY.get_scores Method."

print "\n==TEST 1=="
print "Retrieving scores using defaults.\n"

print osuAPY.get_scores(dev_key, "256754", "", "")

print "\n==TEST 2=="
print "Retrieving scores by user ID.\n"

print osuAPY.get_scores(dev_key, "256754", "2770894", "")

print "\n==TEST 3=="
print "Retrieving scores by mode.\n"

print osuAPY.get_scores(dev_key, "256754", "", "0")

print "\n=SET 4==================================================================="
print "osuAPY.get_user_best Method."

print "\n==TEST 1=="
print "Retrieving user's best plays using defaults. A user ID is required.\n"

print osuAPY.get_user_best(dev_key, "2770894", "", "", "")

print "\n==TEST 2=="
print "Retrieving user's best plays by beatmap mode.\n"

print osuAPY.get_user_best(dev_key, "2770894", "0", "", "")

print "\n==TEST 3=="
print "Retrieving user's best plays by limit.\n"

print osuAPY.get_user_best(dev_key, "2770894", "", "3", "")

print "\n==TEST 4=="
print "Retrieving user's best plays by type (id).\n"

print osuAPY.get_user_best(dev_key, "2770894", "", "", "id")

print "\n==TEST 5=="
print "Retrieving user's best plays by type (string).\n"

print osuAPY.get_user_best(dev_key, "albinohat", "", "", "string")

print "\n=SET 5==================================================================="
print "osuAPY.get_user_recent Method."

print "\n==TEST 1=="
print "Retrieving user recent plays using defaults. A user ID is required.\n"

print osuAPY.get_user_recent(dev_key, "2770894", "", "")

print "\n==TEST 2=="
print "Retrieving user recent plays by beatmap mode.\n"

print osuAPY.get_user_recent(dev_key, "2770894", "0", "")

print "\n==TEST 4=="
print "Retrieving user recent plays by type (id).\n"

print osuAPY.get_user_recent(dev_key, "2770894", "", "id")

print "\n==TEST 5=="
print "Retrieving user recent plays by type (string).\n"

print osuAPY.get_user_recent(dev_key, "albinohat", "", "string")

print "\n=SET 6==================================================================="
print "osuAPY.get_match Method."

print "\n==TEST 1=="
print "Retrieving match info. Both parameters are required.\n"
print osuAPY.get_match(dev_key, "11117046")

print "\nFinished osuAPY Unit Tests"
