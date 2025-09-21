import feedparser
import requests
import os

# --- CONFIG ---
LINKEDIN_RSS = "https://www.linkedin.com/feed/update/urn:li:activity:YOUR_POST_ID?lipi=..."  # Replace with your RSS/feed
LAST_FILE = "last.txt"

# Example: Twitter (via v2 API) and Telegram Bot API
TWITTER_BEARER = os.getenv("TWITTER_BEARER")
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

def get_last_post():
    if os.path.exists(LAST_FILE):
        with open(LAST_FILE, "r") as f:
            return f.read().strip()
    return None

def save_last_post(post_id):
    with open(LAST_FILE, "w") as f:
        f.write(post_id)

def post_to_twitter(text):
    # Simplified — requires Twitter v2 API
    url = "https://api.twitter.com/2/tweets"
    headers = {"Authorization": f"Bearer {TWITTER_BEARER}"}
    data = {"text": text}
    r = requests.post(url, headers=headers, json=data)
    print("Twitter:", r.status_code, r.text)

def post_to_telegram(text):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    data = {"chat_id": TELEGRAM_CHAT_ID, "text": text}
    r = requests.post(url, data=data)
    print("Telegram:", r.status_code, r.text)

def main():
    feed = feedparser.parse(LINKEDIN_RSS)
    if not feed.entries:
        print("No entries found.")
        return
    latest = feed.entries[0]
    post_id = latest.id

    if post_id == get_last_post():
        print("No new post.")
        return

    text = latest.title + "\n" + latest.link
    post_to_twitter(text)
    post_to_telegram(text)
    save_last_post(post_id)

if __name__ == "__main__":
    main()
