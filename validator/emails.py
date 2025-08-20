import requests
import hashlib
import json
from rich import print
def email_check(email):
    with open("validator/email-data.json", "r") as f:
        config = json.load(f)

    def hash_sha256(data):
        return hashlib.sha256(data.encode()).hexdigest()

    def extract_token(pre_check):
        try:
            resp = requests.request(
                method=pre_check["method"],
                url=pre_check["endpoint"],
                headers=pre_check.get("headers"),
                data=pre_check.get("data"),
            )
            return resp.cookies.get(pre_check["cookie_name"])
        except Exception as e:
            print("Pre-check failed:", e)
            return None


    results = []

    for s in config["sites"]:
        name = s["name"]
        method = s.get("method", "GET")
        url = s["uri_check"]
        headers = s.get("headers", {})
        data = s.get("data")
        input_op = s.get("input_operation")
        pre_check = s.get("pre_check")

        account_value = hash_sha256(email) if input_op == "hash-sha256" else email

        url = url.replace("{account}", account_value)
        if data:
            data = data.replace("{account}", account_value)

        if pre_check:
            token = extract_token(pre_check)
            if token:
                for h_key in headers:
                    headers[h_key] = headers[h_key].replace("{csrftoken_value}", token)
                if data:
                    data = data.replace("{csrftoken_value}", token)
                url = url.replace("{csrftoken_value}", token)

        try:
            response = requests.request(method, url, headers=headers, data=data)
            response_text = response.text
            status_code = response.status_code
            e_code = str(s["e_code"])
            m_code = str(s["m_code"])
            e_string = s["e_string"]
            m_string = s["m_string"]



            result = {
                "site": name,
                "url": url,
                "status_code": status_code,
                "is_registered": None,
                "response_text_snippet": response_text[:300],  # Limit large output
            }

            if str(status_code) == e_code and e_string in response_text:
                print(f"[bold red][+][/bold red] {name} URL: {url}")
                result["is_registered"] = True
            elif str(status_code) == m_code and m_string in response_text:
                result["is_registered"] = False
            else:
                result["is_registered"] = "unknown"

            try:
                parsed = response.json()
                result["json_response"] = parsed
            except Exception:
                result["json_response"] = None

            results.append(result)

        except Exception:
            pass


    for e in results:
        try:
            if e["site"] == "Gravatar" and e.get("json_response"):
                gravatar_info = e["json_response"]["entry"][0]
                username = gravatar_info.get("preferredUsername")
                profile_url = gravatar_info.get("profileUrl")
                thumbnail = gravatar_info.get("thumbnailUrl")
                display_name = gravatar_info.get("displayName")

                print("\n👤 Username:", username)
                print("🔗 Profile URL:", profile_url)
                print("🖼️ Thumbnail:", thumbnail)
                print("🪪 Display Name:", display_name)
                print("\n")
        except Exception:
            pass
