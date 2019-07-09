from dateutil.parser import parse
from db_ops import connect_db

# calculate timedeltas
# for x in mycol.find({QUERY},{ "_id": 0, "name": 1, "address": 1 })