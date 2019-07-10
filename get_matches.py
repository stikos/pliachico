import json
import requests


def get_matches(fromDateIn=None, toDateIn=None):
    """
    Gets a range of days in %Y-%d-%M format and gets a JSON response containing a variety of info for the matches
    retrieved. I only need the ID, the time and the result
    :param fromDateIn: The date from which we want to retrieve matches
    :param toDateIn: The date up to when we want to retrieve matches
    :return: The retrieved matches in a list of dicts
    """
    url = "https://api.opap.gr/sb/sport/virtual_soccer/coupon?locale=el&onlyLive=false&marketIds=1%2C18"

    if fromDateIn is not None and toDateIn is not None:
        url += '&' + "fromDate=" + fromDateIn + '&' + "toDate=" + toDateIn

    response = json.loads(requests.get(url).text)

    if "events" in response:
        matches = response["events"]["content"]
        entries = []
        for item in matches:
            entries.append({"id": item["id"],
                            "time": item.get("dt", None),
                            "result": item["scr"]["EndResult"]}) if "scr" in item else None

        return entries

    else:
        raise ValueError
