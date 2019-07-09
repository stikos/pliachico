"""
An experimental app to check for possible ''patterns'' in OPAP's Virtual Football results
"""

from flask import Flask
import requests
import json
import pymongo
import os
import time


app = Flask(__name__)

@app.route('/')
def main_routine():
    live = "false"
    fromDate = "fromDate=" + "2019-07-07" #time.strftime("%Y-%d-%M")
    toDate = "toDate=" + "2019-07-07" #time.strftime("%Y-%d-%M")

    url = "https://api.opap.gr/sb/sport/virtual_soccer/coupon?locale=el&onlyLive="\
            + live\
            + "&marketIds=1%2C18&"\
            + fromDate + '&'\
            + toDate

    response = json.loads(requests.get(url).text)

    if "events" in response:
        matches = response["events"]["content"]
        entries = []
        for item in matches:
            entries.append({"id": item["id"], "time": item["dt"], "result": item["scr"]["EndResult"]})



# # get mongoDB uri depending on the env
# if os.environ["PATH"].startswith("/home/konstantinos/"):
#     import configparser
#     local_config = configparser.ConfigParser()
#     local_config.read('data.ini')
#     mongodb_uri = local_config["CREDS"]["mongodb"]
# else:
#     mongodb_uri = os.environ["MONGODB"]
#
# myclient = pymongo.MongoClient(mongodb_uri)
# mydb = myclient["pliachicoDB"]
# mycol = mydb["matches"]
# x = mycol.insert_many(entries)

    print(entries)