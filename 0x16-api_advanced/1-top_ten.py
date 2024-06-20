#!/usr/bin/python3
"""
Function that queries the Reddit API and prints the titles
of the first 10 hot posts listed for a given subreddit.
"""

import requests

def top_ten(subreddit):
    """
    Function that queries the Reddit API and prints the titles
    of the first 10 hot posts listed for a given subreddit.
    If not a valid subreddit, print None.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "Custom"}

    try:
        # Send GET request to Reddit API
        response = requests.get(url, headers=headers, params={"limit": 10})
        response.raise_for_status()  # Raise exception for bad response status

        # Parse JSON response
        data = response.json()
        posts = data["data"]["children"]

        if not posts:
            print("No posts found.")
            return

        # Print titles of the first 10 hot posts
        for post in posts:
            title = post["data"]["title"]
            print(title)

    except requests.RequestException as e:
        print(f"Error fetching subreddit: {e}")
    except KeyError:
        print(f"Invalid subreddit: {subreddit}")
