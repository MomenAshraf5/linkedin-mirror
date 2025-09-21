import os
import requests

# Twitter secrets from GitHub
TWITTER_BEARER = os.getenv("TWITTER_BEARER")

def post_to_twitter(text):
    url = "https://api.twitter.com/2/tweets"
    headers = {"Authorization": f"Bearer {TWITTER_BEARER}"}
    data = {"text": text}
    r = requests.post(url, headers=headers, json=data)
    print("Twitter:", r.status_code, r.text)

def main():
    post_to_twitter("🚀 Test tweet from GitHub Actions automation!")

if __name__ == "__main__":
    main()
