import pandas as pd
import numpy as np
from pymongo import MongoClient
from dotenv import dotenv_values

# ENV variables here
env_variables = dotenv_values(".env")

# Mongo creds Here
CLIENT = MongoClient(env_variables["MONGO_DB"])
DB = CLIENT["spring"]
HOST = env_variables["HOST"]
PORT = 27017

# Collection names here
NEWS_FEED = "news_feed"
RECCOMMENDATION_FEED ="recommedation_feed"
USER_CONFIG = "user_config"

# FUNCTIONS

def pull_from_db(collection_name:str)-> pd.DataFrame:
    """
    Summary:
    This function will make generic pulls from the database

    Args:
        It will take in the collection name which is type string
    """
    
    collection = DB[collection_name]
    
    cursor = collection.find({})
    
    return pd.DataFrame(list(cursor))

# ---------------------

# NEWS FEED COLLECTION HERE

# ----------------------

df = pull_from_db(NEWS_FEED)



