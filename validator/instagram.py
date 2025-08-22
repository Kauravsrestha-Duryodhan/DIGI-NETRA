import requests
import json
from rich import print


def instafind(email):

    with open("main/check.json", "r") as file:
        config = json.load(file)

    url = config["url"]
    headers = config["headers"]
    payload_key = config["payload_key"]
    data = {payload_key: email}


    response = requests.post(url, headers=headers, data=data)

    try:
        result = response.json()
        contact_email = result.get("contact_point")
        if contact_email:
            print(f"[+] Instagram account found!\n[-] Registered Email: {contact_email}\n")
        else:
            print("[!] No associated Instagram account found.")
    except Exception as e:
        print("[!] Error decoding response:", response.text)

if __name__ == "__main__":
    user_email = input("Enter email or username to check: ")
    if "@" in user_email and "." in user_email:
        print("[+] Valid Mail")
        instafind(user_email)
    else:

        print("[!] Please Enter Valid Email")
