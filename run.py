"""
An experimental app to check for possible ''patterns'' in OPAP's Virtual Football results
"""

from flask import Flask
import requests
from bs4 import BeautifulSoup


# constants
app = Flask(__name__)
url = "https://virtualsports.opap.gr/virtual-results"
match = "event-row not-printed-event res0 extra-results vs-table-row row"
score = "col-md-1 col-sm-4 col-xs-4 hidden-sm hidden-xs vs-no-bg vs-home-score "

page = requests.get(url)
soup = BeautifulSoup(page.text, 'lxml')
matches = soup.findAll("div", class_=match)
print(matches)