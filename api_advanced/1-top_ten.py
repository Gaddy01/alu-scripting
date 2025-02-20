#!/usr/bin/python3
""" top_ten.py """
import requests

def top_ten(subreddit):
    """Prints the titles of the first 10 hot posts listed in a subreddit"""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'MyRedditBot/0.1'}
    params = {'limit': 10}  # Ensure we only get 10 posts

    response = requests.get(url, headers=headers, params=params, allow_redirects=False)

    if response.status_code != 200:
        print(None)
        return
    
    try:
        data = response.json()
        posts = data.get('data', {}).get('children', [])
        if not posts:
            print(None)
            return
        for post in posts:
            print(post['data']['title'])
    except (KeyError, ValueError):
        print(None)
