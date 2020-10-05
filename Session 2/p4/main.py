# Note to future EG volunteers: avoid connecting to the API over the VPN; slowness may be observed.

import requests
import json

api_key = "ca3c26eb1b4d3b51c8f1de0195429c46"

response = requests.get("https://api.themoviedb.org/3/genre/movie/list?api_key=" + api_key)

json_response = json.loads(response.text)

print(json_response)

# print("\nThere are " + str(len(json_response['genres'])) + " available genres in the database.\n")