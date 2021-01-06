import requests
import json

my_access_token = 'cc11693a96d7aa02f9261fe2134d5c6cf3d1abf7'
my_url = 'https://api.github.com/repos/chehine-hub/OpenClassroomAPIV2'
my_headers = {'Content-Type': 'application/json', 'Authorization': 'token {}'.format(my_access_token)}

response = requests.delete(url = my_url, headers = my_headers) 

if str(response.status_code) == "204":
    print(f"Operation done successfully")
else: print(f"ERROR, something went wrong. Error Code {response.status_code}")