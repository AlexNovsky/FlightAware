import base64
import requests

# Creating token and encoding with Base64 encryption
token = f"Bearer {base64.b64encode(b'Software Test Engineer').decode('utf-8')}"

# Setting API URL variable
url = 'https://flightaware.com/about/careers/position/_someURLforAPI_'

# Setting API transaction attributes
headers = {
    "content-type": "application/json",
    "Authorization": token
}
json = {
    "name": "Your Name",
    "email": "Your@email.com"
}

# Posting API call
print(requests.post(url, headers=headers, json=json).text)