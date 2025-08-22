import requests
from rich import print
def facebook():
    url = 'https://www.facebook.com/ajax/login/help/identify.php?'
    email = input("Enter Your Email:- ")
    cookies = {
        'datr': 'baGIaG8syWdTJTq-uEXnaZGm',
    }

    headers = {
        'Host': 'www.facebook.com',
        'Sec-Ch-Ua-Platform': '"Windows"',
        'Accept-Language': 'en-GB,en;q=0.9',
        'Sec-Ch-Ua': '"Not)A;Brand";v="8", "Chromium";v="138"',
        'Sec-Ch-Ua-Mobile': '?0',
        'X-Asbd-Id': '359341',
        'X-Fb-Lsd': 'AVrECuVmCkc',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Accept': '*/*',
        'Origin': 'https://www.facebook.com',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
    }

    data = f'lsd=AVrECuVmClc&email={email}&__a=1'

    response = requests.post(url, cookies=cookies, headers=headers, data=data)
    re = response.text
    print(re)
