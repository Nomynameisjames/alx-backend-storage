#!/usr/bin/env python3
'''
    using the pymongo module to list all items in a mongoDB collection'''
from pymongo import MongoClient


def list_all(mongo_collection):
    db = mongo_collection.find()
    collection = [items for items in db]
    return collection
