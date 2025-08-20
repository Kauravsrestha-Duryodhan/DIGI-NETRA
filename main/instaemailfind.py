import requests
import json
def instafind(username):
    url = "https://www.instagram.com/api/v1/web/accounts/account_recovery_send_ajax/"
    headers = {
        "Host": "www.instagram.com",
        "Content-Type": "application/x-www-form-urlencoded",
        "X-Csrftoken": "asdfgdfghjgfdhg",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36",
        "Accept": "*/*",
        "Referer": "https://www.instagram.com/accounts/password/reset/",
        "Origin": "https://www.instagram.com",
    }
    data = {
        "email_or_username": username
    }
    response = requests.post(url, headers=headers, data=data)
    data = json.loads(response.text)
    email = data.get("contact_point")
    print(f"❤️❤️ Your Instagram Account Email is :- {email}")