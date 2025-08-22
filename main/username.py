import requests
import json
import time
from rich import print
from concurrent.futures import ThreadPoolExecutor, as_completed
from .instaemailfind import instafind as infind
from .scrap import chess
from .scrap import instauser
from .scrap import gitinfo


def load_sites_config(path="main/murl.json"):
    with open(path, 'r') as f:
        return json.load(f)

def check_username_on_site(username, site_name, site_config):
    url = site_config["url"].replace("{username}", username)
    headers = site_config.get("headers", {})
    timeout = site_config.get("timeout_seconds", 5)
    delay = site_config.get("rate_limit_delay", 1)
    allow_redirects = (site_config["redirect_behavior"] == "follow")

    try:
        response = requests.request(
            method=site_config["request_method"],
            url=url,
            headers=headers,
            timeout=timeout,
            allow_redirects=allow_redirects,
        )

        if not site_config["detect_based_on_message"]:
            if response.status_code in site_config["not_found_status_codes"]:
                return site_name, False, None
            return site_name, True, url

        content = response.text
        if site_config["not_found_message"] and site_config["not_found_message"] in content:
            return site_name, False, None
        if site_config["found_message"] and site_config["found_message"] in content:
            return site_name, True, url

        return site_name, None, None
    except requests.RequestException:
        print(f"[!] Error checking {site_name}")
        return site_name, None, None
    finally:
        time.sleep(delay)
        

def main():
    print("[magenta]Enter username to search[/magenta]: ", end="")
    username = input().strip()
    sites = load_sites_config()

    with ThreadPoolExecutor(max_workers=10) as executor:
        futures = [
            executor.submit(check_username_on_site, username, site_name, site_config)
            for site_name, site_config in sites.items()
        ]

        for future in as_completed(futures):
            site_name, result, link = future.result()
            if result is True:
                print(f"[+] Found on {site_name} : {link}")
            elif result is False:
                pass  # Not found
            if site_name.lower() == "instagram":
                print("[magenta][+][/magenta] Running Instagram email lookup...\n")
                infind(username)
                instauser(username)
            elif site_name.lower() == "chess.com":
                chess(username)
            elif site_name.lower() == "github":
                gitinfo(username)
            else:
                # print(f"[?] Could not determine for {site_name}")
                pass

if __name__ == "__main__":
    main()

