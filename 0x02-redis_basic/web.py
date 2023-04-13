#!/usr/bin/env python3
'''import files'''
import requests
import redis

'''
    The core of the function is very simple. It uses the requests module
    to obtain the HTML content of a particular URL and returns it.
'''


client = redis.Redis()


def get_page(url: str) -> str:
    try:
        '''
            using the requests module to obtain html content
        '''
        doc = client.get(url)
        if doc is not None:
            return doc.decode('utf-8')

        response = requests.get(url)
        doc = response.text

        client.set(url, doc, ex=10)
        client.incr(f"count:{url}")

        return doc
    except Exception as e:
        return f"error {e}"


if __name__ == '__main__':

    url = 'http://slowwly.robertomurray.co.uk'
    connect = get_page(url)
    print(connect)
