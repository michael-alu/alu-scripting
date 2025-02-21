#!/usr/bin/python3
"""
This module queries the Reddit API and prints the titles of the first 10 hot posts
listed for a given subreddit.

Prototype:
    def top_ten(subreddit)

If the subreddit is invalid, it prints None.
"""

import requests


def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of the first 10 hot posts for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit to query.
    
    Returns:
        None
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'Python:top_ten:v1.0 (by /u/your_username)'}
    params = {'limit': 10}

    try:
        response = requests.get(url, headers=headers, params=params, allow_redirects=False)
        
        # Check if the request was successful and that it didn't redirect
        if response.status_code == 200:
            data = response.json().get('data')
            if data:
                posts = data.get('children', [])
                for post in posts:
                    print(post['data']['title'])
            else:
                print(None)
        else:
            print(None)
    except Exception:
        print(None)

