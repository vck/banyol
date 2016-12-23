import sqlite3 as sqlite
import re
import records
import os


db = sqlite.connect("banyol.db")
cur = db.cursor()

cur.execute("DROP TABLE IF EXISTS corpora")
cur.execute("""CREATE TABLE corpora(id INTEGER
                PRIMARY KEY AUTOINCREMENT, \
              corpus varchar(100), berkasid INTEGER,
              FOREIGN KEY(berkasid) REFERENCES berkas(id))""")

db.commit()

DB_NAME = "banyol.db"

recordsdb = records.Database("sqlite:///"+DB_NAME)

regex = re.compile("\W+")

def normalizer(w):
    if w.endswith("pdf"):
        return w.split("/")[-1].strip(".pdf").lower()
    return w.split("/")[-1].strip(".")

doc = recordsdb.query("SELECT * FROM berkas")
corpora = doc.all()
parsed_corpora = [normalizer(w.filename) for w in corpora]
cleaned_corpora = [regex.sub(" ", w) for w in parsed_corpora]

for i in range(len(corpora)):
    print "updating corpus={0} with id={1}".format(cleaned_corpora[i], corpora[i].id)
    try:
        db.execute("INSERT INTO corpora(corpus, berkasid) VALUES \
        ('{0}', '{1}')".format(cleaned_corpora[i], corpora[i].id))
    except Exception as err:
        print "unable to update corpora, reason: {}".format(err)
print "corpora table updated!"
db.commit()
