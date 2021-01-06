import requests
import json

my_access_token = 'cc11693a96d7aa02f9261fe2134d5c6cf3d1abf7'
my_url = 'https://api.github.com/user/repos'
my_body = {'name': 'OpenClassroomAPI', 'description': 'test_repo'}
my_headers = {'Content-Type': 'application/json', 'Authorization': 'token {}'.format(my_access_token)}

response = requests.post(url = my_url, data = json.dumps(my_body), headers = my_headers) 

if str(response.status_code) == "201":
    print(f"Operation done successfully")
else: print(f"ERROR, something went wrong. Error Code {response.status_code}")
