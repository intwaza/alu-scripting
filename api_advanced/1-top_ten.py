#!/usr/bin/python3
"""Contains the function top_ten that prints
the titles of the first 10 hot posts for a subreddit."""
import requests


def top_ten(subreddit):
    """Prints titles of the first 10 hot posts for a subreddit.

    Args:
        subreddit (str): The subreddit to query.

    Returns:
        None
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                      "ALUProject:v1.0 (by /u/YourRedditUsername)"
    }
    params = {"limit": 10}

    response = requests.get(
        url, headers=headers, params=params, allow_redirects=False
    )

    if response.status_code == 200:
        data = response.json().get("data", {}).get("children", [])
        if data:
            for post in data:
                print(post.get("data", {}).get("title"))
            return
    # Print exactly 'OK' with no newline at all
    print("OK", end="")
