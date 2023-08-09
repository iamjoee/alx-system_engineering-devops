#!/usr/bin/python3
"""Function to print titles of top 10 hot posts on a given Reddit subreddit."""
import requests


def top_ten(subreddit):
    """Print the titles of the top 10 hot posts on a given subreddit."""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 404:
        print("None")
        return

    try:
        data = response.json().get("data")
        children = data.get("children")

        for post in children[:10]:
            print(post.get("data").get("title"))

    except Exception:
        pass


if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        top_ten(sys.argv[1])
