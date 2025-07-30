from pymongo import MongoClient
from datetime import datetime
import os
from dotenv import load_dotenv
load_dotenv()

class search_write:
    def __init__(self):
        self.client=MongoClient(os.getenv("MONGO_URI"))
        self.db=self.client[os.getenv("MONGO_DB_NAME")]
        self.collection=self.db[os.getenv("MONGO_COLLECTION_NAME")]


    def log_search(self, search_type, params, results_count:int):
        allowed_search_types = ["by title", "by year", "by genre",
                                "by actor", "by years (from... to...)",
                                "by genre and years"]
        if search_type not in allowed_search_types:
            return
        log_entry={
            "timestamp": datetime.now().isoformat(),
            "search_type": search_type,
            "params": params,
            "results_count": results_count
        }
        self.collection.insert_one(log_entry)