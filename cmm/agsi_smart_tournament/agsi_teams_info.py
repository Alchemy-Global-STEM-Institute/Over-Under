import requests
import json
import random

baseurl = "https://www.robotevents.com/api/v2/"
payload={}
"""headers = {
    'Accept': 'application/json',
    'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiIzIiwianRpIjoiY2Y4OWI1NDQ0NzlkNWUxODcwY2I1MTRiYzg0YTEwYWM3MTAxNzBkM2VkNGM4M2U2YTQyNjQzOWI1MWU4OTQzMjc4MjNiMmI1M2M0ZGMyZjAiLCJpYXQiOjE2NjkyNTU3NTAuMjc0NzgxLCJuYmYiOjE2NjkyNTU3NTAuMjc0Nzg0MSwiZXhwIjoyNjE2MDI2OTUwLjI2NzA1NzksInN1YiI6IjEwOTc3MCIsInNjb3BlcyI6W119.iV2fyTAvm7IvmAl7QBRmX-XRc-puPwB65kAUcVlWJAxGf6jt8hia-fK_Lz3OlaqG7bU-V_aEGojrq7hwVfeVO4sdt81YIRBa_sE59-1O1u3JUisR6k98Rk1xdD-nFfKoK4PVSBQtUVUUuY3-SwKcXAS8nY_6s9hDj2lFDf6tlSZIcmL5ru9DQehnC4oqYc0kyz_HwjhA5eSbGGOi9YEStVfcGf3EJzJ6C4PF_mOuOjrfcMM2o99od1JzukiPlH4-k9tmOLS5ICyAgttGXwsYkBu1Nh2t7uAdUnQbOrSQgSJdqROuyGkFx-YPL3gccladGvr4yRC00s4oa8ANoRhXrjYq19-9zhitw8ZKeCieCGIvKm9twVTkPgU7vfBEpDQE8tz1Kg-4vdu2Vqe4MzOXXYw7mbhU3rmJapAw-8lPNbPugN7rH87JIXB-CvaYSBCAZ7F5BVAsSOgXoRZC2PSXCUKi-i6hscvxSLR4UrK_bUZM08jEczEGiTcOjjdUtzbfphV_PsdomOt1sfui9FqUHeDTxN_JuNetg2zwcpOopamHJeBMJ8Htt9N0JWw-wdD8EzztwqeT-hmlWsHTLTxfnzkcsHCGucwB3k602-1f-EdQzvZQGPp__6f1R7H4ktD0RWNHMYBVF5oput9DbiBs3GzH9JGdXvF_FUjsDdNsVK8'
    }"""

headers = {
    'Accept': 'application/json',
    'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiIzIiwianRpIjoiNzY5ZDkyYTkwNTE1YjM5MzA4YmExZWE4MDVlOGVhN2Y5YzA1MDFmZmYyMjkyYjgxYzY1YTdlY2EyNGYxY2IxNmZmMGJhNmNhYWYxZDNhMjMiLCJpYXQiOjE2OTQ0NTkwMTkuOTY2Mjg1LCJuYmYiOjE2OTQ0NTkwMTkuOTY2Mjg4MSwiZXhwIjoyNjQxMjMzODE5Ljk1NzEzMzgsInN1YiI6IjExNzg2MiIsInNjb3BlcyI6W119.Qb-TT2SPOM_ooQplquuQmHp4LxpIB4yFlCryiLlcJhung5hRcI61rxv0L6PeioNgX2iRP7px4OAaTvSrlnqjemvoIAWcDKA7NjycEr6dWIdQ3kjneQZicBpJ9orGNDE4oBJKIEheKl4JSPvmpoeXhpFeMDh74E6DTTie2qAB96sof19z3BNSeie2ZRyqNpR2BCb6k_kLP4wNewwvgYupaviASzLguMPLZem-XEyBdl5y915sOg4oOkegtjoN6Eb0hm-nMFIZYeFjMFlnHbvo9vpi50ptAaPv9itAhxVNixZLHb1eaL7OzoalAni4pbixQO0qv9URXCGW6o4-zOYOcV-G2qF30CIqDyts0hObQBGqFNBJFDoVoMhpsrvEkeZ98LAjYEF-eRSYOuyS37KkrKHm86kiaxcFGMDl1tBy2UnyBr-bX8M2lB3B2VcZNriHIGRdXugL0G2XBnGQxJz_Chyp1vvd9gY8-a_2gm9bXkpTSODZBFtCAVBp0MSn3qx7iqXJcUo8im-DXP3R6Nl-7k1sEZikGKz8ajyBXG6Xu8VEVnRWxY3PxPbT4tbOcetiXIClJxf58X3p6Rtjxjngq1GHXX0Vy3ewuN7PS6r1V9EpVl87KwM_o1y-oge8BHeYlfbhsPa1s2RmzwstVqjRm2Ry0-GI6f1S7GunXlvGJBk'
            }
team = "57711X"
season = 173
event = ''
region = "Tennessee"

def average(list):
    return sum(list) / len(list)

def get_team_details(team):
    team_info_url = baseurl+"teams?number[]="+team+"&program[]=1"
    team_info_response = requests.request("GET", team_info_url, headers=headers, data=payload)
    team_details = team_info_response.json()['data'][0]
    team_id = team_details['id']
    team_number = team_details['number']
    team_name = team_details['team_name']
    team_robot_name = team_details['robot_name']
    team_organization = team_details['organization']
    team_grade = team_details['grade']
    team_region = team_details['location']['region']
    team_city = team_details['location']['city']
    team_programs = team_details['program']['code']
    return team_id, team_number, team_name, team_robot_name, team_organization, team_grade, team_region, team_city, team_programs

def get_region_events(region):
    i = 0
    s = 0
    event_ids = {}
    div_ids = []
    region_info_url = baseurl+"events?season[]="+str(season)+"&region="+region
    events_info_response = requests.request("GET", region_info_url, headers=headers, data=payload)
    meta_event_data = events_info_response.json()['meta']
    maxPage = meta_event_data['last_page']
    ##last_page = events_info_response['meta']
    ##print(region_events)
    while i < maxPage:
        i = i +1
        page_url = region_info_url+"&page=" + str(i)
        events_data = requests.request("GET", page_url, headers=headers, data=payload)
        event_data_full = events_data.json()['data']
        for events in event_data_full:
            event_ids[events['id']] = []
            s = s + 1
            if events['program']['code'] == "VRC":
                for ids in events['divisions']:
                    event_ids[events['id']].append(ids['id'])
    return event_ids

def get_events_division_matches(event_dict):
    i = 0
    for k, v in event_dict.items():
        for x in v:
            matches_url = baseurl+"events/"+str(k)+"/divisions/"+str(x)+"/matches"
            matches_meta_request = requests.request("GET", matches_url, headers=headers, data=payload)
            matches_meta_data = matches_meta_request.json()['meta']
            maxPage = matches_meta_data['last_page']
            while i < maxPage:
                i = i + 1
                pageurl = matches_url+"?page=" + str(i)
                matches_request = requests.request("GET", pageurl, headers=headers, data=payload)
                matches_data = matches_request.json()['data']
                print("-------------------------------------------------")
                print(matches_meta_data)
                print("-------------------------------------------------")
                print(pageurl)
                print("-------------------------------------------------")
                print(matches_data)
                print("-------------------------------------------------")


def test_get_team_events(team):
    team_id = get_team_details(team)[0]
    team_events_url = baseurl+"teams/"+str(team_id)+"/events?season[]="+str(season)
    team_events_response = requests.request("GET", team_events_url, headers=headers, data=payload)
    team_event_details = team_events_response.json()
    ids = []
    for data in team_event_details['data']:
        if data['level'] == "Other" or data['level'] == "State" or data['level'] == "Regional":
            ids.append(data['id'])
        else:
            pass
        #print(data['id'])
    #print(ids)
    print(ids)
    print(team_id)
    return ids, team_id

def get_team_events(team):
    team_id = get_team_details(team)[0]
    team_events_url = baseurl+"teams/"+str(team_id)+"/events?season[]="+str(season)
    team_events_response = requests.request("GET", team_events_url, headers=headers, data=payload)
    team_event_details = team_events_response.json()
    ids = []
    for data in team_event_details['data']:
        if data['level'] == "Other" or data['level'] == "State" or data['level'] == "Regional":
            ids.append(data['id'])
        else:
            pass
        #print(data['id'])
    #print(ids)
    return ids

def get_match_details(team):
    ids = get_team_events(team)
    team_id = get_team_details(team)[0]
    all_event_matches = []
    for id in ids:
        team_matches_url = baseurl+"teams/"+str(team_id)+"/matches?event[]="+str(id)
        team_matches_response = requests.request("GET", team_matches_url, headers=headers, data=payload)
        team_matches_details = team_matches_response.json()
        if len(team_matches_details['data']) != 0:
            all_event_matches.append(team_matches_details['data'])
    all_team_score = []
    all_opp_score = []
    matches_result = []
    per_match_info = []
    for event in all_event_matches:
        event_name = event[0]['event']['name']
        match_event_code = event[0]['event']['code']
        #print(event)
        #print(event_name)
        #print(match_event_code)
        #print("-------------------------------------------------------------------------------------------------")
        for matches in event:
            match_info = {}
            match_name = matches['name']
            #print(event_name)
            #print(match_name)
            #print("-------------------------------------------------------------------------------------------------")
            if team in str(matches['alliances'][0]):
                #print("I am Blue")
                team_color = "blue"
                team_score = int(matches['alliances'][0]['score'])
                opp_score = int(matches['alliances'][1]['score'])
                #print(matches['alliances'][0])
                #print("My Score "+str(team_score))
                #print("Opp Score "+str(opp_score))
                if team_score > opp_score and team_color == "blue":
                    match_won = True
                    #print(match_won)
                    matches_result.append(match_won)
                else:
                    match_won = False
                    #print(match_won)
                    matches_result.append(match_won)
            else:
                team_color = "red"
                team_score = int(matches['alliances'][1]['score'])
                opp_score = int(matches['alliances'][0]['score'])
                #print("I am Red")
                #print(matches['alliances'][1])
                #print("My Score "+str(team_score))
                #print("Opp Score "+str(opp_score))
                if team_score > opp_score and team_color == "red":
                    match_won = True
                    #print(match_won)
                    matches_result.append(match_won)
                else:
                    match_won = False
                    #print(match_won)
                    matches_result.append(match_won)
            #print("-------------------------------------------------------------------------------------------------")
            if team_score != 0:
                all_team_score.append(team_score)
            if opp_score != 0:
                all_opp_score.append(opp_score)
            for info in ["event_name","match_name","team_color","team_score","opp_score","match_won"]:
                match_info[info] = eval(info)
            #print(match_info)
            #print("-------------------------------------------------------------------------------------------------")  
            per_match_info.append(match_info)
    return matches_result, all_team_score, all_opp_score, per_match_info
        #print(per_match_info)

def test_get_match_details(team):
    ids_team_id = test_get_team_events(team)
    ids = ids_team_id[0]
    team_id = ids_team_id[1]
    all_event_matches = []
    for id in ids:
        team_matches_url = baseurl+"teams/"+str(team_id)+"/matches?event[]="+str(id)
        team_matches_response = requests.request("GET", team_matches_url, headers=headers, data=payload)
        team_matches_details = team_matches_response.json()
        if len(team_matches_details['data']) != 0:
            all_event_matches.append(team_matches_details['data'])
    all_team_score = []
    all_opp_score = []
    matches_result = []
    per_match_info = []
    for event in all_event_matches:
        event_name = event[0]['event']['name']
        match_event_code = event[0]['event']['code']
        #print(event)
        #print(event_name)
        #print(match_event_code)
        #print("-------------------------------------------------------------------------------------------------")
        for matches in event:
            match_info = {}
            match_name = matches['name']
            #print(event_name)
            #print(match_name)
            #print("-------------------------------------------------------------------------------------------------")
            if team in str(matches['alliances'][0]):
                #print("I am Blue")
                team_color = "blue"
                team_score = int(matches['alliances'][0]['score'])
                opp_score = int(matches['alliances'][1]['score'])
                #print(matches['alliances'][0])
                #print("My Score "+str(team_score))
                #print("Opp Score "+str(opp_score))
                if team_score > opp_score and team_color == "blue":
                    match_won = True
                    #print(match_won)
                    matches_result.append(match_won)
                else:
                    match_won = False
                    #print(match_won)
                    matches_result.append(match_won)
            else:
                team_color = "red"
                team_score = int(matches['alliances'][1]['score'])
                opp_score = int(matches['alliances'][0]['score'])
                #print("I am Red")
                #print(matches['alliances'][1])
                #print("My Score "+str(team_score))
                #print("Opp Score "+str(opp_score))
                if team_score > opp_score and team_color == "red":
                    match_won = True
                    #print(match_won)
                    matches_result.append(match_won)
                else:
                    match_won = False
                    #print(match_won)
                    matches_result.append(match_won)
            #print("-------------------------------------------------------------------------------------------------")
            if team_score != 0:
                all_team_score.append(team_score)
            if opp_score != 0:
                all_opp_score.append(opp_score)
            for info in ["event_name","match_name","team_color","team_score","opp_score","match_won"]:
                match_info[info] = eval(info)
            #print(match_info)
            #print("-------------------------------------------------------------------------------------------------")  
            per_match_info.append(match_info)
    return matches_result, all_team_score, all_opp_score, per_match_info
"""def get_calc_stats(team):
    matches_result = get_match_details(team)[0]
    all_team_score = get_match_details(team)[1]
    all_opp_score = get_match_details(team)[2] 
    per_match_info = get_match_details(team)[3]
    matches_result_lost_count = matches_result.count(False)
    matches_result_won_count = matches_result.count(True)
    #match_info = {event_name : }
    #print(match_info)
    #print("average_team_score")
    average_team_score = round(average(all_team_score))
    average_opp_score = round(average(all_opp_score))
    team_top_score = max(all_team_score)
    opp_top_score = max(all_opp_score)
    team_bottom_score = min(all_team_score)
    opp_bottom_score = min(all_opp_score)
    total_matches_played = len(matches_result)
    win_percent = int(round((matches_result_won_count / total_matches_played)*100))
    calculated_info = {}
    for info in ["average_team_score",
    "average_opp_score",
    "team_top_score",
    "opp_top_score",
    "team_bottom_score",
    "opp_bottom_score",
    "matches_result_won_count",
    "matches_result_lost_count",
    "total_matches_played",
    "win_percent"]:
        calculated_info[info] = eval(info)
    return calculated_info"""

def test_get_calc_stats(team):
    all_results = get_match_details(team)
    matches_result = all_results[0]
    all_team_score = all_results[1]
    all_opp_score = all_results[2] 
    per_match_info = all_results[3]
    matches_result_lost_count = matches_result.count(False)
    matches_result_won_count = matches_result.count(True)
    #match_info = {event_name : }
    #print(match_info)
    #print("average_team_score")
    average_team_score = round(average(all_team_score))
    average_opp_score = round(average(all_opp_score))
    team_top_score = max(all_team_score)
    opp_top_score = max(all_opp_score)
    team_bottom_score = min(all_team_score)
    opp_bottom_score = min(all_opp_score)
    total_matches_played = len(matches_result)
    win_percent = int(round((matches_result_won_count / total_matches_played)*100))
    calculated_info = {}
    for info in ["average_team_score",
    "average_opp_score",
    "team_top_score",
    "opp_top_score",
    "team_bottom_score",
    "opp_bottom_score",
    "matches_result_won_count",
    "matches_result_lost_count",
    "total_matches_played",
    "win_percent"]:
        calculated_info[info] = eval(info)
    return calculated_info