import requests
import random
from bs4 import BeautifulSoup


def paste(email):

    dork = f"site:pastebin.com \"{email}\""

    ua_list = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 17_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/123.0.6312.52 Mobile/15E148 Safari/604.1"
    ]


    links = []
    found_count = 0


    headers = {"User-Agent": random.choice(ua_list)}
    google_url = f"https://www.google.com/search?q={dork}"
    response = requests.get(google_url, headers=headers)

    soup = BeautifulSoup(response.text, 'html.parser')
    search_results = soup.find_all('div', class_='tF2Cxc')

    for result in search_results:
        link = result.find('a')['href']
        links.append(link)

    for link in links:
        raw_link = link.replace('https://pastebin.com/', 'https://pastebin.com/raw/')
        r = requests.get(raw_link, headers=headers)

        if email.lower() in r.text.lower():
            print(f"[FOUND] {link}")
            found_count += 1
        else:
            continue

    if found_count == 0:
        print("[INFO] No paste found.")

