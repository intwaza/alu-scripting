#!/usr/bin/python3
"""Prints the title of the first 10 hot posts listed for a given subreddit"""

import requests


def top_ten(subreddit):
    """Main function"""
    URL = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    HEADERS = {"User-Agent": "PostmanRuntime/7.35.0"}

    try:
        RESPONSE = requests.get(URL, headers=HEADERS, allow_redirects=False)
        # DEBUG: Print status code
        print(f"DEBUG: Status Code = {RESPONSE.status_code}")
        # DEBUG: Print response text (first 200 chars)
        print(f"DEBUG: Response = {RESPONSE.text[:200]}")
        if RESPONSE.status_code != 200:
            print(None)
            return
        json_data = RESPONSE.json()
        HOT_POSTS = json_data.get("data").get("children")
        for post in HOT_POSTS:
            print(post.get('data').get('title'))
    except Exception as e:
        print(f"DEBUG: Exception = {e}")
        print(None)


# Test it
if __name__ == '__main__':
    print("=== Testing programming ===")
    top_ten('programming')
    print("\n=== Testing fake subreddit ===")
    top_ten('this_is_a_fake_subreddit')
