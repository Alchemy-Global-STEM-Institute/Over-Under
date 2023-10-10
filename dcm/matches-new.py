#!/usr/bin/python3

import requests
import json


def get_scores(myName):
    url_base = 'https://www.robotevents.com/api/v2/teams/' +str(myName) + '/matches?'
    url_get = 'season%5B%5D=173&round%5B%5D=2'
    avgWin  =0 
    myWinPoints =0 
    myWonMatches =0
    avgLoss  =0
    myLostPoints =0 
    myLostMatches =0
    averageScore = 0
    winPCT = 0 
    maxPage = 0 
    myValues = ''
    totalMatches = 0
    matchString = ''
    url = url_base + url_get
    
    key = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiIzIiwianRpIjoiODdkNTVjNjRjMGEwMDZlYTQ2N2E1NGQ4MWYxYWVlZmVlMzU2ZmFlY2VjNzZlZTNhMDhmN2YwYzY0YWJmOTM0MTNjYzU0NGQ2ODM5NTI2OWYiLCJpYXQiOjE2NzUxOTcwNDEuOTA3NjY5MSwibmJmIjoxNjc1MTk3MDQxLjkwNzY3MjksImV4cCI6MjYyMTk2ODI0MS44OTY1NDIxLCJzdWIiOiIxMDM0ODgiLCJzY29wZXMiOltdfQ.jPNW8cbBYQ5f_NbCwpOqDITK5DxCcF4iS8crsvQFrUD12Z13Dnlm4nBzpyQMOOyyyOrMCHQdKznnA0CNoOYf5h6BEcm3jdoyGHTqlGQJgi_zMUnm_107lTJVKCH477VY0qmdz9l1pw0bsNQno4Iq1NDEKlbbkEPBM_yHUK9WH8CZXJNYEwWY6LyZcFHvPyhIYFa_At6nqqGCQdq2rcj2zQBQbHixpZlZ2TvBJt62AcLl8w3ZRg0UgekBaXJrxvE9zpdPP_mZswDzhB3Qz70pVUpTOxsWP5m6NMVnQ3Xbsx5UMFQlqfbA80Zfeqy6l6MxRWYpyVGvBy1T1oSo3teAaXNQExX8hkDDvgP5ig9HmRNG1xgknJ2YJ4rErXB1yN5wFj1mfI8GbnqBdhAxqUmpEQJwh1fA-7d5vd0DiCcKC417eFylckV2yeXD8kVEEMvxN07TbFcq5AhkEju6i6mcB7-pAO0VAK3dwKOKwiYLUUUuVP2xl-KF1cdl62rod0JF3HBXyaOBb5U06aH3-740IN9gQYWu1XC3QpF76j_vGsdw7AMl-BnvkjWLvDA8r7h4i8uKLz79KnWvbgK7BhgxBKf5WZ_DLAgp33c-ynEotJ6m9Ga1CbVIE_YoGO0Re6VyER8OTONHuWlN7sgx5s0oSeDGAJ1gobu1DJZpbC2B_EE'
    
    
    headers = {'Content-Type': 'application/json',
               'Authorization': 'Bearer {0}'.format(key)}
    
    
    ##print(url)
    response = requests.get(url, headers=headers)
    json_data = json.loads(response.text)
    matchData =json_data['data']
    metaData=json_data['meta']
    
    
    nextPage= metaData['next_page_url']
    maxPage= metaData['last_page']
    totalMatches = metaData['total']
    redscore=0
    bluescore=0
    me = str(myName)
    myColor = ''
   
    ##print("I am")
    ##print(me) 
    
    i=1
    j=1.5
    maxPage = maxPage + 1 
    while i < maxPage:
        i = i + 1
        print("top of loop")
        for m in matchData:

            url = url_base + "page=" + str(i) + "&" + url_get
            #print(m)
            for adata in m['alliances']:
                matchString= str(j) + " of " + str(totalMatches)
                j=j+.5
                #print(adata)
                #print(adata['color'])
                if adata['color'] == "blue": bluescore= adata['score']
                if adata['color'] == "red": redscore= adata['score']
                for myteams in adata['teams']:
                    if me == str( myteams['team']['id']):
                        myColor = adata['color']
                        print("I found my self") 
                    print(myteams['team']['id'])
            print ("I am " + myColor)        
            if myColor == 'red':
               if bluescore > redscore: 
                   print("I lost")
                   myLostPoints = myLostPoints + redscore
                   myLostMatches = myLostMatches + 1
               else: 
                   print("I won")
                   myWinPoints = myWinPoints + redscore
                   myWonMatches = myWonMatches + 1
            if myColor == 'blue':
               if bluescore < redscore: 
                   print("I lost")
                   myLostPoints = myLostPoints + redscore
                   myLostMatches = myLostMatches + 1
        
               else: 
                   print("I won")
                   myWinPoints = myWinPoints + bluescore
                   myWonMatches = myWonMatches + 1
        
        
            print("Blue Score " + str(bluescore))
            print("Red Score " + str(redscore))
        
            bluescore=0
            redscore=0
                       
                    
                
            print("-------------------"+ matchString +" ----------------")
        print(url)            
        response = requests.get(url, headers=headers)
        json_data = json.loads(response.text)
        matchData =json_data['data']
        metaData=json_data['meta']
        print("bottom  of loop")
        
    avgWin = myWinPoints / myWonMatches
    avgLoss = myLostPoints / myLostMatches
    averageScore = (myWinPoints + myLostPoints) / (myWonMatches + myLostMatches)
    if myWonMatches + myLostMatches ==0:
        winPCT = 0
    else:
        winPCT = (myWonMatches / (myWonMatches + myLostMatches))*100

    print("My Average Win " + str(avgWin))
    print("My Average Loss " + str(avgLoss))
    print("My Average SCore " + str(averageScore))
    print("My Win %% is " + str(winPCT))
    print(myWonMatches + myLostMatches)

    myValues = [avgWin, avgLoss, averageScore, winPCT, myWonMatches + myLostMatches]

    return(myValues)
