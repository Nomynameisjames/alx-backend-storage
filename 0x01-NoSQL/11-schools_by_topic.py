#!/usr/bin/env python3
'''
    using the pymongo module to find an items in a mongoDB collection
'''


def schools_by_topic(mongo_collection, topic):
    '''
        query the collection using the find method
    '''
    db = mongo_collection.find({'topics': topic})

    return db
