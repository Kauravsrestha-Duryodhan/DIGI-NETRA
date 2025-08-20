import requests
def hudson(email):
    api = "https://cavalier.hudsonrock.com/api/json/v2/osint-tools/search-by-email"

    response = requests.get(api, headers={'api-key': 'ROCKHUDSONROCK'}, params={'email': email})

    print(response.text)
