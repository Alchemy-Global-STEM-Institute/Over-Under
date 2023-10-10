#!/usr/bin/python3

import requests
import json


url_base = 'https://www.robotevents.com/api/v2/teams/130544/awards'

url = url_base 

key = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiIzIiwianRpIjoiODdkNTVjNjRjMGEwMDZlYTQ2N2E1NGQ4MWYxYWVlZmVlMzU2ZmFlY2VjNzZlZTNhMDhmN2YwYzY0YWJmOTM0MTNjYzU0NGQ2ODM5NTI2OWYiLCJpYXQiOjE2NzUxOTcwNDEuOTA3NjY5MSwibmJmIjoxNjc1MTk3MDQxLjkwNzY3MjksImV4cCI6MjYyMTk2ODI0MS44OTY1NDIxLCJzdWIiOiIxMDM0ODgiLCJzY29wZXMiOltdfQ.jPNW8cbBYQ5f_NbCwpOqDITK5DxCcF4iS8crsvQFrUD12Z13Dnlm4nBzpyQMOOyyyOrMCHQdKznnA0CNoOYf5h6BEcm3jdoyGHTqlGQJgi_zMUnm_107lTJVKCH477VY0qmdz9l1pw0bsNQno4Iq1NDEKlbbkEPBM_yHUK9WH8CZXJNYEwWY6LyZcFHvPyhIYFa_At6nqqGCQdq2rcj2zQBQbHixpZlZ2TvBJt62AcLl8w3ZRg0UgekBaXJrxvE9zpdPP_mZswDzhB3Qz70pVUpTOxsWP5m6NMVnQ3Xbsx5UMFQlqfbA80Zfeqy6l6MxRWYpyVGvBy1T1oSo3teAaXNQExX8hkDDvgP5ig9HmRNG1xgknJ2YJ4rErXB1yN5wFj1mfI8GbnqBdhAxqUmpEQJwh1fA-7d5vd0DiCcKC417eFylckV2yeXD8kVEEMvxN07TbFcq5AhkEju6i6mcB7-pAO0VAK3dwKOKwiYLUUUuVP2xl-KF1cdl62rod0JF3HBXyaOBb5U06aH3-740IN9gQYWu1XC3QpF76j_vGsdw7AMl-BnvkjWLvDA8r7h4i8uKLz79KnWvbgK7BhgxBKf5WZ_DLAgp33c-ynEotJ6m9Ga1CbVIE_YoGO0Re6VyER8OTONHuWlN7sgx5s0oSeDGAJ1gobu1DJZpbC2B_EE'


headers = {'Content-Type': 'application/json',
           'Authorization': 'Bearer {0}'.format(key)}


#print(url)
response = requests.get(url, headers=headers)
json_data = json.loads(response.text)
eventData =json_data['data']
metaData=json_data['meta']


nextEvent= metaData['next_page_url']
maxEvent= metaData['last_page']

numAwards= len(eventData)
print(numAwards)
for event in eventData:
    print(event["qualifications"])
