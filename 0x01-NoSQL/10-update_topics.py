#!/usr/bin/env python3
'''
    using the pymongo module to changes all topics of a school
    document based on the name:
'''


def update_topics(mongo_collection, name, topics):
    '''
        using the update_many  method to update
        items in a collection
    '''
    db = mongo_collection.update_many(
                                {'name': name},
                                {'$set': {'topic': topics}}
                )

    return db
