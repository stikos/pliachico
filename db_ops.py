import pymongo
import os


def connect_db():
    """
    Establishes a connection that depends on the env and return the database
    :return: The DB
    """
    # get mongoDB uri depending on the env
    if os.environ["PATH"].startswith("/home/konstantinos/"):
        import configparser
        local_config = configparser.ConfigParser()
        local_config.read('data.ini')
        mongodb_uri = local_config["CREDS"]["mongodb"]
    else:
        mongodb_uri = os.environ["MONGODB"]

    myclient = pymongo.MongoClient(mongodb_uri)
    return myclient["pliachicoDB"]


def update_db(entries, my_db):
    """
     Gets a list of entries and inserts them in the mongoDB
    :param entries: list of dicts, the matches with their id, time and result fields
    :param my_db: mongodb object, the database
    :return: None
    """
    mycol = my_db["matches"]
    x = mycol.insert_many(entries)