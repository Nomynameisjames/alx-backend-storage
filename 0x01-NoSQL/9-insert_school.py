#!/usr/bin/env python3
'''
    using the pymongo module to insert items in a mongoDB collection
'''


def insert_school(mongo_collection, **kwargs):
    '''
        using the insert_one  method to insert items into a collection
    '''
    db = mongo_collection.insert_one(kwargs)
    return db.inserted_id
