"""
An experimental app to check for possible ''patterns'' in OPAP's Virtual Football results
"""

from celery import Celery
from flask import Flask
import schedule
import time
from db_ops import connect_db
from routines import retrieval

pliachico = Flask(__name__)

# TODO
def make_celery(app):
    celery = Celery(
        app.import_name,
        backend=app.config['CELERY_RESULT_BACKEND'],
        broker=app.config['CELERY_BROKER_URL']
    )
    celery.conf.update(app.config)

    class ContextTask(celery.Task):
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return self.run(*args, **kwargs)

    celery.Task = ContextTask
    return celery



def wrapStringInHTML(body, latest_update):
    wrapper = """
    <html>
        <head>
            <title>%s</title>
        </head>
        <body>
            <img src="https://www.aiobot.com/wp-content/uploads/2018/12/money-with-sneaker-bot.png" alt="Pliachico" 
                height="200" width="200"></img><br>
            <p>%s</p>
            <p>DB last updated @: %s</p>
        </body>
    </html>"""

    whole = wrapper % ("Πλιάτσικο v1.0", body, latest_update)
    return whole

@pliachico.route('/')
def greet():
    body = "Θα ενημερώνεσαι στο email σου για τυχόν *ζεματιστές* εξελίξεις<br>Μαζί θα φέρουμε τη βροχή. Προσεχώς..."
    latest_update = open("latest.entry", 'r').read()
    return wrapStringInHTML(body, latest_update)

# print("Initiated")
# mydb = connect_db()
# retrieval(mydb)
# schedule.every(5).minutes.do(retrieval, mydb)
#
# while True:
#     schedule.run_pending()
#     time.sleep(1)
