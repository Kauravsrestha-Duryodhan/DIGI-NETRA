import requests
import json
import re 
from bs4 import BeautifulSoup
def chess(username):
    

    url = f"https://www.chess.com/member/{username}"
    response = requests.get(url)
    try:
        print("\n=== Chess.com Profile Information ===\n")
        
        soup = BeautifulSoup(response.text, 'html.parser')
        profilehead=soup.find("div", class_="profile-header-details-item").text.strip()
        print("✔️  Joined On Chess:- ",profilehead)
        name=soup.find("div", class_="profile-card-name").text.strip()
        
        plocation=soup.find("div", class_="profile-card-location").text.strip()
        print("✔️  Joined On Chess: ",profilehead)
        print("👤 Profile Name    : ",name)
        print("📍 User Location   : ", plocation)
    except:
        print("Check Your Internet Or Unable To Extract Data")
    
def instauser(username):
    print("\n=== Instagram Profile Information ===\n")
    headers_id = {
        'Host': 'www.instagram.com',
        'Sec-Ch-Ua-Platform': '"Windows"',
        'Accept-Language': 'en-GB,en;q=0.9',
        'Sec-Ch-Ua': '"Not)A;Brand";v="8", "Chromium";v="138"',
        'Sec-Ch-Ua-Model': '""',
        'Sec-Ch-Ua-Mobile': '?0',
        'X-Asbd-Id': '359341',
        'X-Ig-D': 'www',
        'X-Fb-Lsd': 'AVrpG3JvYVI',
        'Sec-Ch-Prefers-Color-Scheme': 'dark',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Sec-Ch-Ua-Platform-Version': '""',
        'Accept': '*/*',
        'Origin': 'https://www.instagram.com',
        'Sec-Fetch-Site': 'same-origin',
    }

    data_id = f'\r\n\r\n\r\nroute_urls[0]=%2F{username}%2F&route_urls[1]=%2Fstories%2F{username}%2F%3Fr%3D1&routing_namespace=igx_www%24a%2487a091182d5bd65bcb043a2888004e09&__a=1&__hs=20288.HYP%3Ainstagram_web_pkg.2.1...0&__comet_req=7&lsd=AVrpG3JvYVI'

    response_id = requests.post('https://www.instagram.com/ajax/bulk-route-definitions/', headers=headers_id, data=data_id, verify=True)

    match = re.search(r'"id"\s*:\s*"(\d+)"', response_id.text)
    if not match:
        print("User ID not found!")
        exit()

    userid = match.group(1)

    headers_profile = {
        'Host': 'www.instagram.com',
        'Sec-Ch-Ua-Platform': '"Windows"',
        'X-Root-Field-Name': 'fetch__XDTUserDict',
        'Sec-Ch-Ua': '"Not)A;Brand";v="8", "Chromium";v="138"',
        'Sec-Ch-Ua-Model': '""',
        'Sec-Ch-Ua-Mobile': '?0',
        'X-Ig-App-Id': '936619743392459',
        'X-Fb-Lsd': 'AVrpG3JvIkk',
        'Content-Type': 'application/x-www-form-urlencoded',
        'X-Csrftoken': '4HAnA7JRaAhCK-yl2myRLS',
        'Accept-Language': 'en-GB,en;q=0.9',
        'X-Fb-Friendly-Name': 'PolarisProfilePageContentQuery',
        'X-Bloks-Version-Id': 'e1456a3f58800541d8a2ea65b55937920007fee744eed6e5b1a7723cbe417e5f',
        'X-Asbd-Id': '359341',
    }

    data_profile = f'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36\r\n\r\n\r\n\r\n&variables=%7B%22id%22%3A%22{userid}%22%2C%22render_surface%22%3A%22PROFILE%22%7D&doc_id=24098904923132686'

    response = requests.post('https://www.instagram.com/graphql/query', headers=headers_profile, data=data_profile, verify=True)

    data = response.json()

    with open("instadata.json", "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

    try:
        bio = data["data"]["user"]["biography"]
        fullname = data["data"]["user"]["full_name"]
        purl = data["data"]["user"]["hd_profile_pic_url_info"]["url"]
        fcount = data["data"]["user"]["following_count"]
        mcount = data["data"]["user"]["media_count"]
        uid = data["data"]["user"]["id"]
        followcount = data["data"]["user"]["follower_count"]
        linked = data["data"]["user"]["biography_with_entities"]["entities"]
        hashtags = [e["hashtag"] for e in linked if e["hashtag"]]
        users = [e["user"] for e in linked if e["user"]]
        print("📍 Bio Of A Profile   : ", bio)
        print("📛 Fullname           : ", fullname)
        print("🧑 Profile Pic URL    : ", purl)
        print("🙏 Following          : ", fcount)
        print("👍 Follwers           : ",followcount)
        print("📝 Posts              : ", mcount)
        print("🪪 User ID            : ", uid)
        print("📌 Hashtags:")
        for i, h in enumerate(hashtags, 1):
                print(f"{i}. #{h['name']} (ID: {h['id']})")
        print("👤 Users:")
        for i, u in enumerate(users, 1):
            print(f"{i}. @{u['username']} (ID: {u['id']})")
    except Exception as e:
        print("❌ Failed to parse profile data:", e)
    
def gitinfo(username):
    url = f"https://github.com/{username}"
    
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        print("\n=== GitHub Profile Information ===\n")
        try:
            profilebio = soup.find("div", class_="p-note user-profile-bio mb-3 js-user-profile-bio f4").div.text.strip()
            print("🪪 Bio        :", profilebio)
        except:
            print("Bio        : Not found")
        try:
            org = soup.find("span", class_="p-org").div.text.strip()
            print("🏢 Org        :", org)
        except:
            print("Org        : Not found")
        try:
            country = soup.find("span", class_="p-label").text.strip()
            print("🚩 Country    :", country)
        except:
            print("Country    : Not found")
        try:
            links = [a['href'] for a in soup.find_all("a", class_="Link--primary") if a.has_attr('href')]
            print("\n🔗 Links:")
            for i , links in enumerate(links,1):
                print(f"[{i}] {links}")
        except:
            print("Links      : Not found")
        try:
            prname = soup.find("span", class_="p-name").text.strip()
            print("📛 Full Name  :", prname)
        except:
            print("Full Name  : Not found")
        try:
            uname = soup.find("span", class_="vcard-username").text.strip()
            print("👤 Username   :", uname)
        except:
            print("Username   : Not found")
        try:
            msg = soup.find("div", class_="user-status-message-wrapper").div.text.strip()
            print("👍 Status     :", msg)
        except:
            print("Status     : Not found")
        try:
            follow = [span.text.strip() for span in soup.find_all("span", class_="text-bold")]
            if len(follow) >= 2:
                print(f"  Followers: {follow[0]}")
                print(f"  Following: {follow[1]}")
            else:
                for i, count in enumerate(follow, 1):
                 print(f"  Count {i}: {count}")
        except:
            print("Follow     : Not found")
        try:
            pimg = soup.find("img", class_="avatar")['src']
            print("❤️ Avatar URL :", pimg)
        except:
            print("Avatar URL : Not found")

    except Exception as e:
        print("❌ Unable to extract:", str(e))

