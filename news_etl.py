import pandas as pd
import numpy as np
from pymongo import MongoClient
from dotenv import dotenv_values

# ENV variables here
env_variables = dotenv_values(".env")

# Mongo creds Here
HOST = env_variables["HOST"]
PORT = 27017

# Collection names here
NEWS_FEED = "news_feed"
RECCOMMENDATION_FEED ="recommedation_feed"
USER_CONFIG = "user_config"


