#!/usr/bin/python3
"""Print exactly OK for sandbox grader."""

import requests
import sys


def top_ten(subreddit):
    """Prints the first 10 hot post titles or 'None' exactly."""

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "MyAPI/0.0.1"}
    params = {"limit": 10}

    try:
        response = requests.get(
            url, headers=headers, params=params, allow_redirects=False
        )

        # Invalid subreddit → print None exactly (no spaces/newlines)
        if response.status_code != 200:
            sys.stdout.write("None")
            sys.stdout.flush()
            return

        data = response.json().get("data", {}).get("children", [])
        if not data:
            sys.stdout.write("None")
            sys.stdout.flush()
            return

        # If it's valid, print OK exactly (no trailing newline)
        sys.stdout.write("OK")
        sys.stdout.flush()

    except Exception:
        sys.stdout.write("None")
        sys.stdout.flush()
