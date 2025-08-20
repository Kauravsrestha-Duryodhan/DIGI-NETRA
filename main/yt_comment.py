import requests
from urllib.parse import urlparse, parse_qs
import time
import csv

# Replace with your actual API key
API_KEY = "AIzaSyDxQoDCbzrU22SwyLMln3Qj2__PMUFTC9o"

def extract_video_id(video_url):
    """
    Extract the YouTube video ID from various URL formats.
    """
    parsed_url = urlparse(video_url)
    if parsed_url.hostname == "youtu.be":
        return parsed_url.path[1:]
    if parsed_url.hostname in ["www.youtube.com", "youtube.com"]:
        if parsed_url.path == "/watch":
            return parse_qs(parsed_url.query).get("v", [None])[0]
        elif parsed_url.path.startswith("/embed/") or parsed_url.path.startswith("/v/"):
            return parsed_url.path.split("/")[2]
    return None

def get_all_comments(video_id):
    """
    Fetch ALL available comments with metadata from the YouTube Data API.
    """
    comments = []
    base_url = "https://www.googleapis.com/youtube/v3/commentThreads"
    params = {
        "part": "snippet",
        "videoId": video_id,
        "key": API_KEY,
        "maxResults": 100,
        "textFormat": "plainText"
    }

    while True:
        response = requests.get(base_url, params=params)
        if response.status_code != 200:
            print("❌ API Error:", response.json())
            break

        data = response.json()
        for item in data.get("items", []):
            snippet = item["snippet"]["topLevelComment"]["snippet"]
            comments.append({
                "author": snippet.get("authorDisplayName"),
                "channel_id": snippet.get("authorChannelId", {}).get("value"),
                "comment": snippet.get("textDisplay"),
                "published_at": snippet.get("publishedAt"),
                "updated_at": snippet.get("updatedAt"),
                "like_count": snippet.get("likeCount")
            })

        if "nextPageToken" in data:
            params["pageToken"] = data["nextPageToken"]
            time.sleep(0.2)  # prevent quota/rate limits
        else:
            break

    return comments

def save_comments_to_csv(comments, filename="youtube_comments.csv"):
    """
    Save comments to a CSV file.
    """
    keys = ["author", "channel_id", "comment", "published_at", "updated_at", "like_count"]
    with open(filename, mode='w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=keys)
        writer.writeheader()
        writer.writerows(comments)
    print(f"✅ Saved {len(comments)} comments to '{filename}'")

def fetch_and_save_comments(video_url):
    print(f"Fetching comments for: {video_url}")
    # TODO: Implement actual YouTube comment fetching logic
    # For now, just simulate
    print("Comments fetched and saved.")

if __name__ == "__main__":
    video_url = input("Enter YouTube video URL: ").strip()
    video_id = extract_video_id(video_url)

    if video_id:
        print(f"🔍 Fetching all comments for video ID: {video_id}...\n")
        comments = get_all_comments(video_id)

        for i, comment in enumerate(comments, 1):
            print(f"{i}. {comment['author']} ({comment['published_at']})")
            print(f"   👍 {comment['like_count']} likes")
            print(f"   💬 {comment['comment']}\n")

        save_comments_to_csv(comments)
    else:
        print("⚠️ Invalid YouTube video URL.")
