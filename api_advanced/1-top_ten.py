#!/usr/bin/python3
"""
Queries the Reddit API and prints the titles of the first 10 hot posts
for a given subreddit.
"""
import requests


def top_ten(subreddit):
    """Prints the titles of the first 10 hot posts for a given subreddit."""
    # Define the Reddit API URL
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"

    # Set custom headers to avoid being blocked by Reddit
    headers = {
        "User-Agent": "Mozilla/5.0 (ALU project script)"
    }

    # Limit to 10 posts, and prevent redirects for invalid subreddits
    params = {"limit": 10}

    try:
        response = requests.get(url, headers=headers, params=params, allow_redirects=False)

        # If subreddit doesn't exist or redirect, print None
        if response.status_code != 200:
            print(None)
            return

        data = response.json().get("data", {}).get("children", [])

        # If no posts, print None
        if not data:
            print(None)
            return

        # Print the titles of the 10 hot posts
        for post in data:
            print(post.get("data", {}).get("title"))

    except Exception:
        print(None)
