import json
import time
import requests


def get_matches(fromDateIn=None, toDateIn=None):
    """
    Gets a range of days in %Y-%d-%M format and gets a JSON response containing a variety of info for the matches
    retrieved. I only need the ID, the time and the result
    :param fromDateIn: The date from which we want to retrieve matches
    :param toDateIn: The date up to when we want to retrieve matches
    :return: The retrieved matches in a list of dicts
    """
    live = "false"
    fromDate = "fromDate=" + time.strftime("%Y-%d-%M") if not fromDateIn else "fromDate=" + fromDateIn
    toDate = "toDate=" + time.strftime("%Y-%d-%M") if not toDateIn else "toDate=" + toDateIn

    url = "https://api.opap.gr/sb/sport/virtual_soccer/coupon?locale=el&onlyLive=" \
          + live \
          + "&marketIds=1%2C18&" \
          + fromDate + '&' \
          + toDate

    response = json.loads(requests.get(url).text)

    if "events" in response:
        matches = response["events"]["content"]
        entries = []
        for item in matches:
            entries.append({"id": item["id"], "time": item["dt"], "result": item["scr"]["EndResult"]})

    return entries