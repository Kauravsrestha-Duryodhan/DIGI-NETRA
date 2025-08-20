import requests
import json
def instafind(query):
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
        "email_or_username": query
    }
    response = requests.post(url, headers=headers, data=data)
    print("\n🔃 Checking Account On Instagram\n")
    print(" If Status = ❌ fail Then Your Account is In Trouble or Account Did Not Exists \n If Status = ✅ ok Then Account Exists")
    try:
        data = response.json()
        with open("insta.json", "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
        print("👁️  Account Status :" , data.get("status"))
    except:
         print("🤦‍♂️🤦   Account Did Not Exists or Unable To Retrive Data")