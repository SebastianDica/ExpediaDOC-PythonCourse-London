# Note to future EG volunteers: avoid connecting to the API over the VPN; slowness may be observed.

import http.client
import json

api_key = 'ca3c26eb1b4d3b51c8f1de0195429c46'

connection = http.client.HTTPSConnection('api.themoviedb.org')
connection.request('GET', '/3/genre/movie/list?api_key='+ api_key)
response = connection.getresponse()
response_data = response.read()
connection.close()

print(response_data)