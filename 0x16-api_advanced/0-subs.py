
#!/usr/bin/python3
"""Function to query subscribers on a given Reddit subreddit."""
import requests

def number_of_subscribers(subreddit):
    """Return the total number of subscribers on a given subreddit."""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        "User-Agent": "MyRedditBot/1.0"  # Set your custom User-Agent here
    }
    response = requests.get(url, headers=headers)
    
    if response.status_code == 404:
        return 0
    
    try:
        data = response.json()
        subscribers = data['data']['subscribers']
        return subscribers
    except (KeyError, ValueError):
        return 0

if __name__ == '__main__':
    subreddit_name = "programming"
    subscribers = number_of_subscribers(subreddit_name)
    print("The subreddit '{}' has {} subscribers.".format(subreddit_name, subscribers))

