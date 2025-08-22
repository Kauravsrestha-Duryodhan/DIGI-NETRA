import requests
import json
from rich import print

email = input("Enter your email: ")
url = 'https://api2.sololearn.com/v2/authentication/user'
headers = {
    'Host': 'api2.sololearn.com',
    'Content-Type': 'application/json',
    'Accept': 'application/json',
    'Authorization': 'Bearer eyJhbGciOiJFUzI1NiIsInR5cCI6IkpXVCJ9.eyJzaWQiOiJ7XCJJbnN0YW5jZUlkXCI6NTQwNjMwMTQsXCJVc2VySWRcIjowLFwiTmlja25hbWVcIjpudWxsLFwiRGV2aWNlSWRcIjo5OTQ2MzI2NSxcIkNsaWVudElkXCI6MTE0MyxcIlBsYXRmb3JtSWRcIjo0LFwiTG9jYWxlSWRcIjoxLFwiQXBwVmVyc2lvblwiOlwiMC4wLjAuMFwiLFwiSXNQcm9cIjpmYWxzZSxcIlBsYW5Db25maWd1cmF0aW9uSWRcIjoxLFwiQ29udGV4dElkXCI6MSxcIkdlbmVyYXRpb25cIjpcIjUxYzQ5ZTlkLTBmYmYtNDUyMi1iYmZmLTM5NGI0YzQ2NjcxMFwiLFwiQ291bnRyeUNvZGVcIjpudWxsfSIsImp0aSI6IjkzZDg2MGY5LTNlOTYtNGI4YS1hOTVlLTZhZGFmYzljNTliMyIsImh0dHA6Ly9zY2hlbWFzLm1pY3Jvc29mdC5jb20vd3MvMjAwOC8wNi9pZGVudGl0eS9jbGFpbXMvcm9sZSI6IlB1YmxpYyIsIm5iZiI6MTc1NDQ4NjkzMywiZXhwIjoxNzU0NDkwNTMzLCJpc3MiOiJTb2xvTGVhcm4uU2VjdXJpdHkuQmVhcmVyIiwiYXVkIjoiU29sb0xlYXJuLlNlY3VyaXR5LkJlYXJlciJ9.qzSR_QhyRYOz1ej_s72226ugFloJdcdNnbGh0GiNg_hw2qpnAYCu2zyJmvHHMkaiQ2PCaiAGRnQb1cmFyc8Wvg',

}

json_data = {
    'email': f'{email}',
    'password': 'kkdjksnknskfndnf',
    'name': 'chandu',
    'subject': '',
}

response = requests.post(url, headers=headers, json=json_data)

data = response.json()
description = data.get("invalidParams", [{}])[0].get("description")
print(description)