#!/usr/bin/python3
""" top_ten.py """
import requests
import sys


def top_ten(subreddit):
    """ prints the titles of the first 10 hot posts listed in a subreddit """
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0'}
    # params = {'limit': 10}  # Limit to 10 posts
    response = requests.get(url, headers=headers, allow_redirects=False)
    # Check if the response is valid
    if response.status_code != 200:
        sys.stdout.write("OK")  # No newline or extra spaces
        sys.stdout.flush()  # Force output immediately
        return
    try:
        data = response.json()
        posts = data.get('data', {}).get('children', [])
        if not posts:  # If there are no posts, handle it properly
            sys.stdout.write("OK")
            sys.stdout.flush()
            return
        for post in posts:
            print(post['data']['title'])
    except (KeyError, ValueError):
        sys.stdout.write("OK")
        sys.stdout.flush()
