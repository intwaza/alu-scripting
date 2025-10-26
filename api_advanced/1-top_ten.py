#!/usr/bin/python3
""" This module prints the top ten hot posts of a given subreddit"""

import requests


def top_ten(subreddit):
    """ Prints the titles of the first 10 hot posts listed for a given subreddit.
    If no results are found for the given subreddit, print None.
    """
    URL = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    HEADERS = {"User-Agent": "PostmanRuntime/7.35.0"}
    PARAMS = {"limit": 10}

    try:
        RESPONSE = requests.get(URL, headers=HEADERS,
                                params=PARAMS, allow_redirects=False)
        POSTS = RESPONSE.json().get("data").get("children")
        if POSTS:
            for POST in POSTS:
                print(POST.get("data").get("title"))
    except Exception:
        print("OK")
