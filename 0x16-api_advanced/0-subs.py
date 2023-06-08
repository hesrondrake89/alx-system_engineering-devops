#!/usr/bin/python3
""" A function to fetch subscriber information from a specific subreddit on Reddit"""
import requests

def number_of_subscribers(subreddit):
    
    req = requests.get(
        "https://www.reddit.com/r/{}/about.json".format(subreddit),
        headers={"User-Agent": "Custom"},
    )

    if req.status_code == 200:
        return req.json().get("data").get("subscribers")
    else:
        return 0
