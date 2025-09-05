import requests
import os
from dotenv import load_dotenv

load_dotenv()

pixela_endpoint = 'https://pixe.la/v1/users'
USERNAME = os.getenv('PIXELUSERNAME')
TOKEN = os.getenv('TOKEN')

user_params = {
    "token" : TOKEN,
    "username" : USERNAME,
    "agreeTermsOfService" : os.getenv('AGREETERMSOFSERVICE'),
    "notMinor" : os.getenv('NOTMINOR')
}

# Create a user
"""response = requests.post(url=pixela_endpoint, json=user_params)

print(response.status_code)
print(response.text)"""

graph_endpoint = f'{pixela_endpoint}/{USERNAME}/graphs'

graph_config = {
    "id":'gym1',
    "name": "Gym Tracking",
    "unit": "Exercices",
    "type": "float",
    "color":"ajisai"
}

headers = {
    "X-USER-TOKEN":TOKEN
}

# Post a new graph
"""
graph_response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)

print(graph_response.text)"""

# Update a field in the graph
"""requests.put(url=f"{graph_endpoint}/gym1", headers=headers, json={"unit":"Exercices"})"""

# Post a pixel

pixel_post_config=  {
    "date":'20250819',
    "quantity":"7.5"
}

pixel_post_response = requests.post(url=f'{graph_endpoint}/gym1', headers=headers,json=pixel_post_config)

print(pixel_post_response.text)
print('https://pixe.la/v1/users/juda-tech/graphs/gym1.html')