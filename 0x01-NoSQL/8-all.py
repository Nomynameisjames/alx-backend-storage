#!/usr/bin/env python3
'''
    using the pymongo module to list all items in a mongoDB collection
'''
from typing import List


def list_all(mongo_collection) -> List:
    '''
        query the collection using the find method
    '''
    db = mongo_collection.find()
    collection = [items for items in db]
    return collection
