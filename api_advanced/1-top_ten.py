#!/usr/bin/python3
"""
Fetches and prints the titles of the first 10 hot posts
for a given subreddit.
"""
import requests


def top_ten(subreddit):
    """Prints the titles of the first 10 hot posts or None if invalid."""

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "MyAPI/0.0.1"}
    params = {"limit": 10}

    # Prevent redirects (important for invalid subreddits)
    response = requests.get(url, headers=headers, params=params, allow_redirects=False)

    # Check validity
    if response.status_code != 200:
        print("None")
        return

    try:
        posts = response.json().get("data", {}).get("children", [])
        if not posts:
            print("None")
            return

        for post in posts[:10]:
            print(post.get("data", {}).get("title"))

    except Exception:
        print("None")
