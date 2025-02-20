#!/usr/bin/python3
"""
This module queries the Reddit API to retrieve information 
about a given subreddit, including the number of subscribers 
and the top 10 hot posts.

Functions:
- number_of_subscribers(subreddit): Returns the number of subscribers 
  for a given subreddit.
- top_ten(subreddit): Prints the titles of the first 10 hot posts 
  listed for a given subreddit.
"""

import requests

def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the number of subscribers for a given subreddit.
    
    Parameters:
    subreddit (str): The name of the subreddit to query.
    
    Returns:
    int: The number of subscribers if the subreddit is valid, otherwise 0.
    
    Notes:
    - Uses the Reddit API endpoint `https://www.reddit.com/r/{subreddit}/about.json`.
    - Sets a custom User-Agent to avoid `Too Many Requests` errors.
    - Ensures redirects are not followed to prevent invalid subreddit handling.
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'custom-script/1.0'}  # Setting a custom User-Agent
    
    response = requests.get(url, headers=headers, allow_redirects=False)
    
    if response.status_code == 200:
        data = response.json()
        return data.get("data", {}).get("subscribers", 0)
    else:
        return 0

def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of the first 10 hot posts for a given subreddit.
    
    Parameters:
    subreddit (str): The name of the subreddit to query.
    
    Returns:
    None: Prints the titles of the top 10 hot posts, or 'None' if the subreddit is invalid.
    
    Notes:
    - Uses the Reddit API endpoint `https://www.reddit.com/r/{subreddit}/hot.json`.
    - Sets a custom User-Agent to avoid `Too Many Requests` errors.
    - Ensures redirects are not followed to prevent invalid subreddit handling.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {'User-Agent': 'custom-script/1.0'}  # Setting a custom User-Agent
    
    response = requests.get(url, headers=headers, allow_redirects=False)
    
    if response.status_code == 200:
        data = response.json()
        posts = data.get("data", {}).get("children", [])
        for post in posts:
            print(post.get("data", {}).get("title", ""))
    else:
        print("None")
