
import requests

def recurse(subreddit, hot_list=None, after=None):
    if hot_list is None:
        hot_list = []

    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=100"
    if after:
        url += f"&after={after}"

    headers = {'User-Agent': 'Custom User Agent'}  # Set a custom User-Agent header
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        posts = data.get('data', {}).get('children', [])
        if posts:
            hot_list.extend([post['data']['title'] for post in posts])
            next_after = data['data']['after']
            if next_after:
                return recurse(subreddit, hot_list, next_after)
            else:
                return hot_list
        else:
            return None
    else:
        return None
