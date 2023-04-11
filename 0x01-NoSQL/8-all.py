#!/usr/bin/env python3
'''
    using the pymongo module to list all items in a mongoDB collection'''
from pymongo import MongoClient
from typing import List
'''def connect():
    client = MongoClient(host="localhost", port=27017)
    return client'''


def list_all(mongo_collection) -> List:
    db = mongo_collection.find()
    collection = [items for items in db]
    return collection
