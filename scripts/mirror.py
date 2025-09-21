import os
import requests

TWITTER_BEARER = os.getenv("TWITTER_BEARER")  # Only this is needed

def post_to_twitter(text):
    url = "https://api.x.com/2/tweets"
    headers = {
        "Authorization": f"Bearer {TWITTER_BEARER}",
        "Content-Type": "application/json"
    }
    json_data = {"text": text}
    r = requests.post(url, headers=headers, json=json_data)
    print("Twitter:", r.status_code, r.text)

def main():
    post_to_twitter("🚀 Test tweet from GitHub Actions automation with Bearer Token!")

if __name__ == "__main__":
    main()


