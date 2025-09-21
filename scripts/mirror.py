import os
import requests
from requests_oauthlib import OAuth1

TWITTER_API_KEY = os.getenv("TWITTER_API_KEY")
TWITTER_API_SECRET = os.getenv("TWITTER_API_SECRET")
TWITTER_ACCESS_TOKEN = os.getenv("TWITTER_ACCESS_TOKEN")
TWITTER_ACCESS_TOKEN_SECRET = os.getenv("TWITTER_ACCESS_TOKEN_SECRET")

auth = OAuth1(TWITTER_API_KEY, TWITTER_API_SECRET, TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET)

def post_to_twitter(text):
    url = "https://api.twitter.com/1.1/statuses/update.json"
    data = {"status": text}
    r = requests.post(url, auth=auth, data=data)
    print("Twitter:", r.status_code, r.text)

def main():
    post_to_twitter("🚀 Test tweet from GitHub Actions automation!")

if __name__ == "__main__":
    main()

