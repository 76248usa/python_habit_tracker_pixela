import requests
from datetime import datetime

USERNAME = "elsabe"
TOKEN = "bnmfdsgjkrewty"
GRAPH_ID = "graph1"

pixel_endpoint = "https://pixe.la/v1/users"
user_params = {
    "token": "bnmfdsgjkrewty",
    "username": "elsabe",
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}
graph_config = {
    "id": GRAPH_ID,
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai"
}
headers = {
    "X-USER-TOKEN": TOKEN
}
#graph_endpoint = f"{pixel_endpoint}/{USERNAME}/graphs"
#response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
#print(response.text)

#response = requests.post(url=pixela_endpoint, json=user_params)
#print(response.text)

pixel_creation_endpoint = f"{pixel_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
today = datetime(year=2023, month=11, day=22)
pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "8.4"
}
response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
print(response.text)
#update_endpoint = f"{pixel_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"
#pixel_data = {
#    "quantity": "11"
#}
#response = requests.put(url=update_endpoint, json=pixel_data, headers=headers)
#print(response.text)

#update_endpoint = f"{pixel_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"
#response = requests.delete(url=update_endpoint, headers=headers)
#print(response.text)
