#!/usr/bin/python3
"""
Write a function that queries the Reddit API and returns the number of
subscribers (not active users, total subscribers) for a given subreddit.

Requirements:
    - Prototype: def number_of_subscribers(subreddit)
    - If not a valid subreddit, return 0.
    - NOTE: Invalid subreddits may return a redirect to search results.
      Ensure that you are not following redirects.
"""
import requests


def number_of_subscribers(subreddit):
    """Returns the number of subscribers for a given subreddit"""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        return data["data"]["subscribers"]
    else:
        return 0
