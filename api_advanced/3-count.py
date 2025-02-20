#!/usr/bin/python3
"""
This module queries the Reddit API to retrieve information 
about a given subreddit, including the number of subscribers, 
the top 10 hot posts, all hot post titles recursively, 
and counts of specified keywords in hot post titles.

Functions:
- number_of_subscribers(subreddit): Returns the number of subscribers 
  for a given subreddit.
- top_ten(subreddit): Prints the titles of the first 10 hot posts 
  listed for a given subreddit.
- recurse(subreddit, hot_list=[]): Recursively retrieves all hot post titles 
  for a given subreddit.
- count_words(subreddit, word_list): Recursively counts keyword occurrences 
  in hot post titles and prints them in sorted order.
"""

import requests
from collections import Counter


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


def count_words(subreddit, word_list, counts=None, after=None):
    """
    Recursively queries the Reddit API, counts keyword occurrences in hot post titles,
    and prints them in sorted order.
    
    Parameters:
    subreddit (str): The name of the subreddit to query.
    word_list (list): A list of keywords to count (case-insensitive).
    counts (dict): A dictionary to store word counts (default is None).
    after (str): The pagination parameter for recursion (default is None).
    
    Returns:
    None: Prints word counts sorted by frequency (descending) and alphabetically.
    
    Notes:
    - Uses pagination to recursively fetch all hot posts.
    - Filters out irrelevant words by exact match.
    - Ensures words are counted case-insensitively.
    """
    if counts is None:
        counts = Counter()
    
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=100"
    if after:
        url += f"&after={after}"
    headers = {'User-Agent': 'custom-script/1.0'}
    
    response = requests.get(url, headers=headers, allow_redirects=False)
    
    if response.status_code == 200:
        data = response.json()
        posts = data.get("data", {}).get("children", [])
        
        for post in posts:
            title = post.get("data", {}).get("title", "").lower().split()
            for word in word_list:
                word_lower = word.lower()
                counts[word_lower] += title.count(word_lower)
        
        after = data.get("data", {}).get("after")
        if after:
            return count_words(subreddit, word_list, counts, after)
        
        sorted_counts = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
        for word, count in sorted_counts:
            if count > 0:
                print(f"{word}: {count}")
    else:
        return None
