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

    def log_search(self):
        pass