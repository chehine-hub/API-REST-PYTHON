# Import required modules
import requests
import json
import time
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient

# Set some variables
my_access_token = 'cc11693a96d7aa02f9261fe2134d5c6cf3d1abf7'
my_url = 'https://api.github.com/user/repos'
my_headers = {'Accept': 'application/vnd.github.v3+json', 'Authorization': 'token {}'.format(my_access_token)}

# GET request
response = requests.get(url = my_url, headers = my_headers) 

# Some errors controls
if str(response.status_code) == "200":
    print(f"Operation done successfully")
else: print(f"ERROR, something went wrong. Error Code {response.status_code}")

# Export JSON to file
json_object = json.dumps(response.json(), indent = 4)
timestr = time.strftime("%Y%m%d%H%M%S")
with open('repos_list_' + timestr +'.json', 'w') as outfile:
    outfile.write(json_object)

# Send files to Azure Blob Container
AZURE_STORAGE_CONNECTION_STRING = "DefaultEndpointsProtocol=https;AccountName=storageaccountsandb97e2;AccountKey=CC5TSL5u9xGiWccUSZx4rCL6pTRliXyNMaVUKJzb4GQcnxNV5PZPdFOe/FAO5MlS08SFc6lwPSvsA5GbYie91Q==;EndpointSuffix=core.windows.net"
connect_str = AZURE_STORAGE_CONNECTION_STRING
container_name = "quickstart"
blob_service_client = BlobServiceClient.from_connection_string(connect_str)
#container_client = blob_service_client.create_container(container_name)
local_path = "./"
local_file_name = "repos_list_" + timestr + ".json"
upload_file_path = os.path.join(local_path, local_file_name)

blob_client = blob_service_client.get_blob_client(container=container_name, blob=local_file_name)

print("\nUploading file to Azure Storage :\n\t" + local_file_name)

with open(upload_file_path, "rb") as data:
    blob_client.upload_blob(data)
    print("\nFile Uploaded successfully\n\t")

# Show only available repos
data = json.loads(json_object)
for i in data:
    print(i['name'], '-', i['url'])