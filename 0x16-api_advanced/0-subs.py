#!/usr/bin/python3
"""
 lalkdl
"""


def number_of_subscribers(subreddit):
    '''
        Args:
            subreddit (string): the api endpoint
            Returns (Int): the total number of subreddit
    '''
    from requests import get
    headers = {'user-agent': 'advance-api/1.0.0'}
    sub_url = f"https://www.reddit.com/r/{subreddit}/about.json"

    subscribe = get(sub_url, headers=headers, allow_redirects=False)
    if subscribe.status_code == 200:
        count = subscribe.json()
        return count['data']['subscribers']
    elif subscribe.status_code == 404:
        return 0
    else:
        return 0
