"""
An experimental app to check for possible ''patterns'' in OPAP's Virtual Football results
"""

from flask import Flask
from get_matches import get_matches
from notification import notify
from db_ops import connect_db, update_db

app = Flask(__name__)

def wrapStringInHTML(body):

    wrapper = """<html>
    <head>
    <title>%s</title>
    </head>
    <body><p>Add me on Facebook: <a href=\"%s\">%s</a></p><p>%s</p></body>
    </html>"""

    whole = wrapper % ("Πλιάτσικο v1.0", "https://www.facebook.com/pliachicobot", "Pliachico Botakis", body)
    return  whole



@app.route('/')
def main_routine():
    # notify()
    body = "Θα ενημερώνεσαι για τυχόν *ζεματιστές* εξελίξεις<br>Μαζί θα φέρουμε τη βροχή. Προσεχώς..."
    return wrapStringInHTML(body)
# results = get_matches("2019-07-01", "2019-07-09")
# mydb = connect_db()
# update_db(results, mydb)

# print(results)
