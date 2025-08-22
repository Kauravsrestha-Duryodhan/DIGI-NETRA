import requests
import json
from rich import print
def check_ip_address():
    try:
        print("[magenta]Enter IP Address to search[/magenta]: ", end="")
        IP_ADD = input()
        API_KEY = "f55a0ed4d998cee256cf603954cda0bc"
        url = f"https://api.ipstack.com/{IP_ADD}?access_key={API_KEY}"
        response = requests.get(url)
        data = response.json()
        with open("Data/ip_information.json", "w", encoding="utf-8")as f:
            json.dump(data,f,ensure_ascii=False,indent=4)
        print("[yellow]Ip Information.json Saved in Data Folder[/yellow]\n")
        print(f"IP Address: {data.get('ip')}")
        print(f"Country: {data.get('country_name')}")
        print(f"Region: {data.get('region_name')}")
        print(f"City: {data.get('city')}")
        print(f"Latitude: {data.get('latitude')}")
        print(f"Longitude: {data.get('longitude')}")
        print(f"ISP: {data.get('connection', {}).get('isp')}")
        print(f"Location: {data.get('location', {}).get('geoname_id')}")
        print(f"Language: {data.get('location', {}).get('languages', [{}])[0].get('name')}","\n")
    except Exception:
        print("Error: Unable to validate the IP address. Please check your input or try again later. or check your internet connection.")