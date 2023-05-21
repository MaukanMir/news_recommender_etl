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


