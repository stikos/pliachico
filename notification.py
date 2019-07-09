from fbchat import Client
from fbchat.models import *
import os


def notify(data=None):
    """
    Notify the chosen ones for anything important
    :param data: The news
    :return: None
    """
    # get fb account creds
    if os.environ["PATH"].startswith("/home/konstantinos/"):
        import configparser
        local_config = configparser.ConfigParser()
        local_config.read('data.ini')
        fb_user = local_config["CREDS"]["fb_user"]
        fb_pass = local_config["CREDS"]["fb_pass"]
    else:
        fb_user = os.environ["fb_user"]
        fb_user = os.environ["fb_pass"]

    client = Client(fb_user, fb_pass)

    thread_id = "2384238364965852"
    thread_type = ThreadType.GROUP

    # Form msg from data
    msg = "This is a test message from Pliachico Bot"

    client.send(Message(text=msg), thread_id=thread_id, thread_type=thread_type)
