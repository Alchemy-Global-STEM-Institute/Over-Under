from agsi_teams_info import *
#from concurrent.futures import ThreadPoolExecutor
import asyncio
import time
import datetime
import httpx

header_var = {
    'Accept': 'application/json',
    'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiIzIiwianRpIjoiNzY5ZDkyYTkwNTE1YjM5MzA4YmExZWE4MDVlOGVhN2Y5YzA1MDFmZmYyMjkyYjgxYzY1YTdlY2EyNGYxY2IxNmZmMGJhNmNhYWYxZDNhMjMiLCJpYXQiOjE2OTQ0NTkwMTkuOTY2Mjg1LCJuYmYiOjE2OTQ0NTkwMTkuOTY2Mjg4MSwiZXhwIjoyNjQxMjMzODE5Ljk1NzEzMzgsInN1YiI6IjExNzg2MiIsInNjb3BlcyI6W119.Qb-TT2SPOM_ooQplquuQmHp4LxpIB4yFlCryiLlcJhung5hRcI61rxv0L6PeioNgX2iRP7px4OAaTvSrlnqjemvoIAWcDKA7NjycEr6dWIdQ3kjneQZicBpJ9orGNDE4oBJKIEheKl4JSPvmpoeXhpFeMDh74E6DTTie2qAB96sof19z3BNSeie2ZRyqNpR2BCb6k_kLP4wNewwvgYupaviASzLguMPLZem-XEyBdl5y915sOg4oOkegtjoN6Eb0hm-nMFIZYeFjMFlnHbvo9vpi50ptAaPv9itAhxVNixZLHb1eaL7OzoalAni4pbixQO0qv9URXCGW6o4-zOYOcV-G2qF30CIqDyts0hObQBGqFNBJFDoVoMhpsrvEkeZ98LAjYEF-eRSYOuyS37KkrKHm86kiaxcFGMDl1tBy2UnyBr-bX8M2lB3B2VcZNriHIGRdXugL0G2XBnGQxJz_Chyp1vvd9gY8-a_2gm9bXkpTSODZBFtCAVBp0MSn3qx7iqXJcUo8im-DXP3R6Nl-7k1sEZikGKz8ajyBXG6Xu8VEVnRWxY3PxPbT4tbOcetiXIClJxf58X3p6Rtjxjngq1GHXX0Vy3ewuN7PS6r1V9EpVl87KwM_o1y-oge8BHeYlfbhsPa1s2RmzwstVqjRm2Ry0-GI6f1S7GunXlvGJBk'
            }
team = "57711X"
season = 173
event = ''
region = "Tennessee"
baseurl = "https://www.robotevents.com/api/v2/"

st = datetime.datetime.now()

async def get_match_details(ids):
    all_event_matches = []
    for id in ids:
        team_matches_url = baseurl+"teams/"+str(team_id)+"/matches?event[]="+str(id)
        team_matches_response = requests.request("GET", team_matches_url, headers=headers, data=payload)
        team_matches_details = team_matches_response.json()
        if len(team_matches_details['data']) != 0:
            all_event_matches.append(team_matches_details['data'])
    return all_event_matches

async def process_match_details(all_event_matches):
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

async def request_match_details(baseurl,team_id,id):
   async with httpx.AsyncClient(headers=header_var) as client:
        url = baseurl+"teams/"+str(team_id)+"/matches?event[]="+str(id)
        response = await client.request('GET',url)
        new_response = response.json()
        print(new_response)

ids = get_team_events(team)
team_id = get_team_details(team)[0]

async def main(baseurl,team_id,ids):
    results = await asyncio.gather(*(request_match_details(baseurl,team_id,id) for id in ids))
    await print(results)
    return results
    
asyncio.run(request_match_details(baseurl,team_id,ids))    

if __name__ == '__main__':
    ids = get_team_events(team)
    team_id = get_team_details(team)[0]
    results = main()

et = datetime.datetime.now()
result = et - st
print("Execution time: "+str(result)+" seconds")