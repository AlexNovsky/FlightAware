import base64
import requests

token = f"Bearer {base64.b64encode(b'Software Test Engineer').decode('utf-8')}"
url = 'https://flightaware.com/about/careers/position/_someURLforAPI_'
headers = {
    "content-type": "application/json",
    "Authorization": token
}
json = {
    "name": "Your Name",
    "email": "Your@email.com"
}

print(requests.post(url, headers=headers, json=json).text)