#!/usr/bin/python3

import requests

def top_ten(subreddit):
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
    except Exception as e:
        print(None)

