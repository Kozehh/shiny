import requests
import json
from os import environ

#url = "https://api.rawg.io/api/games/327239"
url = "https://api.rawg.io/api/games/valve-software"
params = {
    "key": environ['RAWG_API_KEY']
}
response = requests.get(url, params=params)

if response.status_code == 200:
    json_data = response.json()
    pretty_json = json.dumps(json_data, indent=4)
    
    with open("output.json", "w") as outfile:
        outfile.write(pretty_json)
    
    print("JSON data saved to 'output.json'")
else:
    print(f"Request failed with status code: {response.status_code}")