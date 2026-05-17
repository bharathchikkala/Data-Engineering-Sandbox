'''
from this mini understood how we use get,post,put,delete even indepth
used websites for this mini project,
PIXELA : https://docs.pixe.la/
Also : https://pixe.la/
'''

import requests
import datetime
PIXELA_ENDPOINT = "https://pixe.la/v1/users"
TOKEN = "tokenkey0212"
USER_NAME = "bharathhchikkala"
GRAPH_ID = "graph20"

user_parameters = {
    "token": TOKEN,  #this is the token key according to the pixela documentation like any alphabet's consider as token key
    "username": USER_NAME,
    "agreeTermsOfService": "yes",
    "notMinor":"yes",
}
# response = requests.post(url=PIXELA_ENDPOINT,json=user_parameters)
# # response.raise_for_status()
# print(response.text)

GRAPH_ENDPOINT = f"{PIXELA_ENDPOINT}/{USER_NAME}/graphs"

graph_parameters = {
    "id": GRAPH_ID,
    "name": "learning Graph",
    "unit": "Hrs",
    "type": "float",
    "color": "sora",
}

headers = {
    "X-USER-TOKEN" : TOKEN,
}

# response = requests.post(url=GRAPH_ENDPOINT, json=graph_parameters,headers=headers)
# print(response.text)

learning_endpoint = f"{PIXELA_ENDPOINT}/{USER_NAME}/graphs/{GRAPH_ID}"

today = datetime.datetime(year=2026, month=5, day=10)
#today = datetime.datetime.now()

learning_parameters = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "1.20",
}

# response = requests.post(url=learning_endpoint, json=learning_parameters,headers=headers)
# print(response.text)

change_data = f"{PIXELA_ENDPOINT}/{USER_NAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"
change_parameters = {
    "quantity": "1.30",
}
response = requests.put(url=change_data, json=change_parameters,headers=headers)
print(response.text)
