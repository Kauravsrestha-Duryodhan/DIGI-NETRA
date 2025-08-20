import requests
import json
from .idcheck import instafind

def search_google(query):
    API_KEY = "AIzaSyDxQoDCbzrU22SwyLMln3Qj2__PMUFTC9o"
    SEARCH_ENGINE_ID = "84a64448a902c4626"

    url = "https://www.googleapis.com/customsearch/v1"
    params = {
        "key": API_KEY,
        "cx": SEARCH_ENGINE_ID,
        "q": query,
        "num": 10
    }

    print("\n🔎 Searching Google...\n")
    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()
        results = data.get("items", [])
        print(f"📄 Top {len(results)} Results for '{query}':\n")
        for index, item in enumerate(results, start=1):
            print(f"{index}. {item['title']}")
            print(f"   {item['link']}\n")
    else:
        print("❌ Google Search Error:", response.status_code)
        print(response.text)

def validate_phone_number(number):
    try:
        API_KEY = "6cddf1fcd79d985e9efc9e140424b888"
        url = "https://apilayer.net/api/validate"
        querystring = {"access_key": API_KEY, "number": number, "country_code": "IN", "format": "1"}

        print("\n📡 Validating phone number...\n")
        response = requests.get(url, params=querystring)
        data = response.json()

        if data.get("valid"):
            print("✅ Phone Number is valid:")
            print(f"📱 Number: {data.get('number')}")
            print(f"🌍 Country: {data.get('country_name')}")
            print(f"📍 Location: {data.get('location')}")
            print(f"📡 Carrier: {data.get('carrier')}")
            print(f"🔌 Line Type: {data.get('line_type')}")
            print(f"🌐 International Format: {data.get('international_format')}")
        else:
            print("❌ Invalid phone number.")
    except Exception as e:
        print("⚠️ Error during phone validation.")
        print("Reason:", e)
def look(query):
    print("\nTAKE A LOOK 👁️")
    print(f"📞 Look For Whatsapp : https://wa.me/{query}")
    print(f"🧑 Look For Telegram : https://t.me/{query}")

def WhatsappInfo(query):
    url = f"https://whatsapp-data1.p.rapidapi.com/number/91{query}"
    print("WAIT......")
    print("Retriving Data From Whatsapp")
    headers = {
	"x-rapidapi-key": "a9aaf84445mshb4bf0006cf29d94p1822f9jsndf0fba00af47",
	"x-rapidapi-host": "whatsapp-data1.p.rapidapi.com"
	}

    response = requests.get(url,headers=headers)

    if response.status_code==200:
        try:
            data = response.json()
    
            with open("whatsapp_data.json", "w", encoding="utf-8") as file:
                json.dump(data, file, ensure_ascii=False, indent=4)
        
            print("❤️ Profile Pic :" , data.get("profilePic"))
            print("📞 Phone Number :" , data.get("phone"))
            print("🔬 About :" , data.get("about\n"))


        except Exception as e:
            print("Failed to Retrive Data:", str(e))

if __name__ == "__main__":
    query = int(input("🔤 Enter your query (Phone Number): "))
    search_google(query)
    print("\n" + "="*50 + "\n")
    validate_phone_number(query)
    look(query)
    WhatsappInfo(query)
    instafind(query)
