from formatter import print_table

class LogStats:
    def __init__(self, log_writer):
        self.collection=log_writer.collection

    def get_popular(self, limit=5):
        row=[
            # {"$group":{
            #     "_id":{"type":"$search_type","params":"$params"},
            #     "count":{"$sum":1}
            # }},
            # {"$sort":{"count":-1}},
            # {"$limit": limit},
            # {"$project":{
            #     "_id":0,
            #     "search_type":"$_id.type",
            #     "params":"$_id.params",
            #     "count":1
            # }}
            {
                "$group": {
                    "_id": {
                        "type": "$search_type",
                        "params": "$params"
                    },
                    "count": {"$sum": 1}
                }
            },
            {"$sort": {"count": -1}},
            {"$limit": limit},
            {
                "$project": {
                    "_id": 0,
                    "search_type": "$_id.type",
                    "params": {
                        "$reduce": {
                            "input": {
                                "$map": {
                                    "input": {"$objectToArray": "$_id.params"},
                                    "as": "p",
                                    "in": {"$toString": "$$p.v"}  # <-- тільки значення
                                }
                            },
                            "initialValue": "",
                            "in": {
                                "$cond": [
                                    {"$eq": ["$$value", ""]},
                                    "$$this",
                                    {"$concat": ["$$value", ", ", "$$this"]}
                                ]
                            }
                        }
                    },
                    "count": 1
                }
            }
        ]
        return list(self.collection.aggregate(row))


    def get_latest(self,limit=5):
        row=[
        #     {"$sort":{"timestamp":-1}},
        #     {"$limit":limit},
        #     {"$project":{
        #     "_id":0,
        #     "search_type":1,
        #     "params":1,
        #     "count":"$results_count"
        # }}
            {"$sort": {"timestamp": -1}},
                    {"$limit": limit},
                    {
                        "$project": {
                            "_id": 0,
                            "search_type": 1,
                            "params": {
                                "$reduce": {
                                    "input": {
                                        "$map": {
                                            "input": {"$objectToArray": "$params"},
                                            "as": "p",
                                            "in": {"$toString": "$$p.v"}  # <-- тільки значення
                                        }
                                    },
                                    "initialValue": "",
                                    "in": {
                                        "$cond": [
                                            {"$eq": ["$$value", ""]},
                                            "$$this",
                                            {"$concat": ["$$value", ", ", "$$this"]}
                                        ]
                                    }
                                }
                            },
                            "count": "$results_count"
                        }
                    }
        ]
        return list(self.collection.aggregate(row))
