#!/usr/bin/python3
"""
This module queries the Reddit API to retrieve the number of subscribers 
for a given subreddit. It handles invalid subreddits by returning 0.
Functions:
- number_of_subscribers(subreddit): Returns the number of subscribers 
  for a given subreddit.
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
