#!/usr/bin/python3
"""Retreiving Post"""


import requests

def top_ten(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {'User-Agent': 'Custom User Agent'}  # Set a custom User-Agent header
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        posts = data.get('data', {}).get('children', [])
        for post in posts:
            print(post['data']['title'])
    else:
        print("None")

