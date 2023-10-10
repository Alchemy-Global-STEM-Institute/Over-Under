#!/usr/bin/python

from matches import *
import requests
import json

newVar = ''
url_base = 'https://www.robotevents.com/api/v2/events/47899/teams?'
url_get  = 'myTeams=false'
State = ''
StateCount = 0
url = url_base +  url_get

out = open("tournInfo.txt","w")

key = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiIzIiwianRpIjoiODdkNTVjNjRjMGEwMDZlYTQ2N2E1NGQ4MWYxYWVlZmVlMzU2ZmFlY2VjNzZlZTNhMDhmN2YwYzY0YWJmOTM0MTNjYzU0NGQ2ODM5NTI2OWYiLCJpYXQiOjE2NzUxOTcwNDEuOTA3NjY5MSwibmJmIjoxNjc1MTk3MDQxLjkwNzY3MjksImV4cCI6MjYyMTk2ODI0MS44OTY1NDIxLCJzdWIiOiIxMDM0ODgiLCJzY29wZXMiOltdfQ.jPNW8cbBYQ5f_NbCwpOqDITK5DxCcF4iS8crsvQFrUD12Z13Dnlm4nBzpyQMOOyyyOrMCHQdKznnA0CNoOYf5h6BEcm3jdoyGHTqlGQJgi_zMUnm_107lTJVKCH477VY0qmdz9l1pw0bsNQno4Iq1NDEKlbbkEPBM_yHUK9WH8CZXJNYEwWY6LyZcFHvPyhIYFa_At6nqqGCQdq2rcj2zQBQbHixpZlZ2TvBJt62AcLl8w3ZRg0UgekBaXJrxvE9zpdPP_mZswDzhB3Qz70pVUpTOxsWP5m6NMVnQ3Xbsx5UMFQlqfbA80Zfeqy6l6MxRWYpyVGvBy1T1oSo3teAaXNQExX8hkDDvgP5ig9HmRNG1xgknJ2YJ4rErXB1yN5wFj1mfI8GbnqBdhAxqUmpEQJwh1fA-7d5vd0DiCcKC417eFylckV2yeXD8kVEEMvxN07TbFcq5AhkEju6i6mcB7-pAO0VAK3dwKOKwiYLUUUuVP2xl-KF1cdl62rod0JF3HBXyaOBb5U06aH3-740IN9gQYWu1XC3QpF76j_vGsdw7AMl-BnvkjWLvDA8r7h4i8uKLz79KnWvbgK7BhgxBKf5WZ_DLAgp33c-ynEotJ6m9Ga1CbVIE_YoGO0Re6VyER8OTONHuWlN7sgx5s0oSeDGAJ1gobu1DJZpbC2B_EE'


headers = {'Content-Type': 'application/json',
           'Authorization': 'Bearer {0}'.format(key)}


#print(url)
response = requests.get(url, headers=headers)
json_data = json.loads(response.text)
recordData =json_data['data']
metaData=json_data['meta']


maxPage= metaData['last_page'] +1

#print(metaData)

i=1
myAwards= ''
while i < maxPage:
   
    myAwards = '' 
    i = i +1
    url = url_base + "page=" + str(i) + "&" + url_get
    #print(url)
    for record  in recordData:
       teamID= str(record['id'])


       skills_url = 'https://www.robotevents.com/api/v2/teams/' +  teamID +'/skills?season%5B%5D=173' 
       skillsResponse = requests.get(skills_url, headers=headers)
       skillsJsonData = json.loads(skillsResponse.text)
       skillsData = skillsJsonData['data']
       bestp = 0
       bestd = 0
       for skills in skillsData:
           #print(skills['team']['name'] + " " + skills['event']['name'] +  " " + skills['type'] +  "  " + str(skills['score']))
           if skills['type'] == "programming":
                if bestp < skills['score']:
                     bestp = skills['score']
           if skills['type'] == "driver":
                if bestd < skills['score']:
                     bestd = skills['score']





       award_url = 'https://www.robotevents.com/api/v2/teams/' +  teamID +'/awards?season%5B%5D=173' 
       awardResponse = requests.get(award_url, headers=headers)
       awardJsonData = json.loads(awardResponse.text)
       awardData = awardJsonData['data']
       myAwards = ''
       for award in awardData: 
           #print(awardData)
           #print(str(record['number']) + " - \"" + str(record['team_name']) + "\" - " +  str(award['qualifications']))
           myAwards = myAwards + str(award['title']) + "  " 
           if "orld" in str(award['qualifications']):
               StateCount = StateCount + 1
               State = "YES"
       if (State == "YES"):
            myAwards = str(StateCount) + "x QUALIFIED  " 
       #newVar = str(get_scores(teamID))
       newVar = ''
       #print(teamID)
       out.write(str(record['number']) + " ; \"" + str(record['team_name']) + "\" ; " + str(bestd) + " ; " + str(bestp) + " ; " + myAwards + "  ; " + newVar ) 
       print(str(record['number']) + " ; \"" + str(record['team_name']) + "\" ; " + str(bestd) + " ; " + str(bestp) + " ; " + myAwards + "  ; " + newVar ) 
       State = ''
       StateCount = 0
       myAwards = ''
    myAwards = ''
    bestp = 0
    bestd = 0
        
    
    response = requests.get(url, headers=headers)
    json_data = json.loads(response.text)
    recordData =json_data['data']
    metaData=json_data['meta']


out.close()
