#!/usr/bin/python3
"""
This module defines functions for fetching and printing
posts from a RESTful API,
and for fetching and saving posts to a CSV file.
"""
import csv
import requests


def fetch_and_print_posts():
    """
    Fetches posts from a RESTful API and prints their titles.

    The function sends a GET request to the API endpoint
    "https://jsonplaceholder.typicode.com/posts" and prints the status code.
    If the request is successful (status code 200), it prints the title of
    each post.
    """
    req = requests.get("https://jsonplaceholder.typicode.com/posts")
    print("Status Code: {}".format(req.status_code))
    if req.status_code == 200:
        for dict in req.json():
            print("{}".format(dict["title"]))


def fetch_and_save_posts():
    """
    Fetches posts from a RESTful API and saves them to a CSV file.

    The function sends a GET request to the API endpoint
    "https://jsonplaceholder.typicode.com/posts". If the request is successful
    (status code 200), it saves the posts to a CSV file named "posts.csv".
    """
    csv_posts = "posts.csv"
    req = requests.get("https://jsonplaceholder.typicode.com/posts")

    if req.status_code == 200:
        posts = req.json()
        fields = ['id', 'title', 'body']
        posts = [{field: post[field] for field in fields} for post in posts]
        with open(csv_posts, 'w', encoding='utf-8') as csv_handle:
            writer = csv.DictWriter(csv_handle, fieldnames=fields)

            writer.writeheader()
            writer.writerows(posts)
