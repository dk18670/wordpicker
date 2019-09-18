import os, csv

import database

from dbutils import *

BASE_DIR = os.path.dirname(__file__)

db = database.Database(WORDPICKER_DB)

db.execute('CREATE TABLE sowpods (word VARCHAR UNIQUE)')

with open(os.path.join(BASE_DIR,'sowpods.txt')) as file:
  reader = csv.reader(file)
  for row in reader:
    word = row[0]
    db.execute('INSERT INTO sowpods (word) VALUES (%s)' % tosql(word))

db.commit()
