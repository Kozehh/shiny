import requests
from os import environ

muscle = 'biceps'
api_url = 'https://api.api-ninjas.com/v1/exercises?muscle={}'.format(muscle)
response = requests.get(api_url, headers={'X-Api-Key': environ['NINJA_API_KEY']})
if response.status_code == requests.codes.ok:
    print(response.text)
else:
    print("Error:", response.status_code, response.text)