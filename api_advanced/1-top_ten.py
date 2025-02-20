#!/usr/bin/python3
""" top_ten.py """
import requests


def top_ten(subreddit):
    """ prints the titles of the first 10 hot posts listed in a subreddit """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'MyRedditScript/0.1'}
    params = {'limit': 10}  # Get only the first 10 hot posts
    
    response = requests.get(url, headers=headers, params=params, allow_redirects=False)
    
    if response.status_code != 200:
        print(None)
        return
    
    data = response.json()
    
    try:
        posts = data['data']['children']
        for post in posts:
            print(post['data']['title'])
    except KeyError:
        print(None)
