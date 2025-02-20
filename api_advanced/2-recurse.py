#!/usr/bin/python3
"""
This module queries the Reddit API to retrieve information 
about a given subreddit, including the number of subscribers, 
the top 10 hot posts, and all hot post titles recursively.
Functions:
- number_of_subscribers(subreddit): Returns the number of subscribers 
  for a given subreddit.
- top_ten(subreddit): Prints the titles of the first 10 hot posts 
  listed for a given subreddit.
- recurse(subreddit, hot_list=[]): Recursively retrieves all hot post titles 
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

def recurse(subreddit, hot_list=[], after=None):
    """
    Recursively queries the Reddit API and retrieves all hot post titles for a given subreddit.
    
    Parameters:
    subreddit (str): The name of the subreddit to query.
    hot_list (list): A list to store hot post titles (default is an empty list).
    after (str): The pagination parameter to get the next set of posts.
    
    Returns:
    list: A list of all hot post titles, or None if the subreddit is invalid.
    
    Notes:
    - Uses the Reddit API endpoint `https://www.reddit.com/r/{subreddit}/hot.json`.
    - Uses pagination with the 'after' parameter to recursively fetch all hot posts.
    - Sets a custom User-Agent to avoid `Too Many Requests` errors.
    - Ensures redirects are not followed to prevent invalid subreddit handling.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=100"
    if after:
        url += f"&after={after}"
    headers = {'User-Agent': 'custom-script/1.0'}
    
    response = requests.get(url, headers=headers, allow_redirects=False)
    
    if response.status_code == 200:
        data = response.json()
        posts = data.get("data", {}).get("children", [])
        hot_list.extend(post.get("data", {}).get("title", "") for post in posts)
        after = data.get("data", {}).get("after")
        
        if after:
            return recurse(subreddit, hot_list, after)
        return hot_list
    else:
        return None
