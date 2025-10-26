#!/usr/bin/python3
"""
Module for querying Reddit API
Contains function to print top 10 hot posts from a subreddit
"""

import requests


def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of the first 10 hot posts
    listed for a given subreddit.
    
    Args:
        subreddit: The name of the subreddit to query
        
    Returns:
        None - prints titles or None if invalid subreddit
    """
    if subreddit is None or not isinstance(subreddit, str):
        print(None)
        return
    
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {"User-Agent": "Mozilla/5.0"}
    
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        
        if response.status_code != 200:
            print(None)
            return
        
        data = response.json().get("data")
        if data is None:
            print(None)
            return
        
        children = data.get("children")
        if children is None:
            print(None)
            return
        
        for post in children:
            print(post.get('data').get('title'))
            
    except Exception:
        print(None)
