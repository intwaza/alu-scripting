#!/usr/bin/python3
"""Prints the title of the first 10 hot posts listed for a given subreddit"""

import requests


def top_ten(subreddit):
    """Main function"""
    URL = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    HEADERS = {"User-Agent": "PostmanRuntime/7.35.0"}
    
    try:
        RESPONSE = requests.get(URL, headers=HEADERS, allow_redirects=False)
        
        # Check if request was successful and not redirected
        if RESPONSE.status_code != 200:
            print(None)
            return
            
        data = RESPONSE.json().get("data")
        if data is None:
            print(None)
            return
            
        HOT_POSTS = data.get("children")
        if HOT_POSTS is None:
            print(None)
            return
        
        # Print each title on a separate line
        for post in HOT_POSTS:
            print(post.get('data').get('title'))
            
    except Exception:
        print(None)
