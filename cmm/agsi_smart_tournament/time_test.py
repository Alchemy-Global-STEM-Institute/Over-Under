from agsi_teams_info import *
import time
import datetime
import multiprocessing as mp

team = "57711N"
season = 173
event = ''
region = "Tennessee"

st = datetime.datetime.now()

#get_calc_stats(team)
##get_team_details(team)
#get_region_events(region)
#get_events_division_matches(event_dict)
get_team_events(team)
##test_get_match_details(team)
#get_match_details(team)
#test_get_calc_stats(team)

et = datetime.datetime.now()#


result = et - st
print("Execution time: "+str(result)+" seconds")