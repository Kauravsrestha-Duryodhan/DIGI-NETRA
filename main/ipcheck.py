import requests
import json
def check_ip_address():
    try:
        IP_ADD = input("Enter the IP address to check: ")
        API_KEY = "f55a0ed4d998cee256cf603954cda0bc"
        url = f"https://api.ipstack.com/{IP_ADD}?access_key={API_KEY}"
        response = requests.get(url)
        data = response.json()
        print(f"IP Address: {data.get('ip')}")
        print(f"Country: {data.get('country_name')}")
        print(f"Region: {data.get('region_name')}")
        print(f"City: {data.get('city')}")
        print(f"Latitude: {data.get('latitude')}")
        print(f"Longitude: {data.get('longitude')}")
        print(f"ISP: {data.get('connection', {}).get('isp')}")
        print(f"Location: {data.get('location', {}).get('geoname_id')}")
        print(f"Language: {data.get('location', {}).get('languages', [{}])[0].get('name')}")
    except Exception:
        print("Error: Unable to validate the IP address. Please check your input or try again later. or check your internet connection.")