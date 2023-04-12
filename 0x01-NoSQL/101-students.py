#!/usr/bin/env python3
'''
    file contains function that returns all students
    sorted by average score:
'''


def top_students(mongo_collection):
    '''
        using aggregation operations to process multiple
        items and return computed results
    '''
    Query_List = [
            {
                "$project":
                {
                    "_id": 1,
                    "name": 1,
                    "topics": [
                        {
                            "title": 1,
                            "score": 1,
                            "averagescore": {
                                "$avg": "topics.score"
                                }
                            }
                        ]
                    }
                },
            {
                    "$sort":
                    {
                        "averagescore": 1
                        }
                    }
            ]
    avg_score = mongo_collection.aggregate(Query_List)
    return list(avg_score)
