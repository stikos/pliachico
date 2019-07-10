from get_matches import get_matches
from db_ops import update_db
from dateutil.parser import parse
import time


def score_alphabet(entries):
    """
    Keeps track of an "alphabet" like file of all possible scores in our DB
    :param entries: New entries to be checked
    :return: None
    """
    raise NotImplementedError


def retrieval(my_db):
    """
    Executed every 5 minutes, the main routine retrieves the latests matches and inserts them in the database
    :param my_db: My mongoDB
    :return: None
    """
    try:
        results = get_matches()
    except ValueError:
        print('Could not get matches. Damn you OPAP.')
        results = None

    if results:
        with open('latest.entry', 'r') as file:
            latest = parse(file.read())

        # reverse order so that the latest event show up first
        results = results[::-1]

        # to be inserted in the db
        new_entries = []

        # in case of an unfinished game, the time field will be null
        if not results[0]:
            results = results[1:]

        for game in results:
            if parse(game["time"]) > latest:
                new_entries.append(game)

            else:
                break

        if new_entries:
            x = update_db(new_entries, my_db)
            print(str(len(new_entries)) + " insertions on " + time.strftime("%Y-%m-%d @ %H:%M:%S"))

        # find the latest entry and write the result in a file
        latest = results[0]["time"]
        with open('latest.entry', 'w') as file:
            file.write(str(latest))