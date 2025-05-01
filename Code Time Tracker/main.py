import requests
from datetime import datetime

# Declaring username and token as global variables
USER_NAME = "madhavi"
TOKEN = ""

# Creating a separate label for the pixela url
pixela_url = "https://pixe.la/v1/users"

# Creating the user params
user_params = {
    "token": TOKEN,
    "username": USER_NAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_url, json=user_params)
# print(response.text)


#Creating seperate labels for creating the graph parameters
graph_endpoint = f"{pixela_url}/{USER_NAME}/graphs"

graph_config = {
    "id": "graph2",
    "name": "My Programming graph",
    "unit": "mins",
    "type": "int",
    "color": "momiji"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# Using the date-time module to automatically updates date for the habit tracker
today = datetime.now()

pixel_creation_url = f"{pixela_url}/{USER_NAME}/graphs/graph2"

pixel_params = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "120"
}
response_1 = requests.post(url=pixel_creation_url, json=pixel_params, headers=headers)
print(response_1.text)
