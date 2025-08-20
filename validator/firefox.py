import requests

def firefox(email):
    try:
        response = requests.post(
            "https://api.accounts.firefox.com/v1/account/status",
            data={"email": email},
            timeout=10
        )
        print("😒 Checking On Firefox.......... ")
        if "false" in response.text:
            print("❌ Firefox: Not registered")
        elif "true" in response.text:
            print("✔️ Firefox: Registered")
        else:
            print("⚠️ Firefox: Unknown (Possible Rate Limit)")

    except requests.RequestException as e:
        print(f"firefox: error ({e})")

