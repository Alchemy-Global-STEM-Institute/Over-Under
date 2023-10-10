from agsi_teams_info import *

average_team_score = 0
average_opp_score = 0
team_top_score = 0
opp_top_score = 0
team_bottom_score = 0
opp_bottom_score = 0
matches_result_won_count = 0
matches_result_lost_count = 0
total_matches_played = 0
win_percent = 0
region = "Tennessee"
event_dict = {47984: [1], 47901: [1]} ##, 48741: [1], 48742: [1], 47778: [1], 48691: [1], 48831: [1], 48832: [1], 49127: [1], 49560: [1], 47729: [1], 48248: [1], 48987: [1], 48990: [1], 49355: [1], 49848: [1], 48744: [1], 48746: [1], 47983: [1], 50819: [1], 48955: [1], 48956: [1], 48992: [1], 48993: [1], 49182: [1], 49534: [1], 48920: [1], 49053: [1], 50076: [1], 47780: [1], 48747: [1], 48748: [1], 48835: [1], 51388: [1], 47899: [1], 47900: [1]

event_ids = []

event_ids = get_events_division_matches(event_dict)
