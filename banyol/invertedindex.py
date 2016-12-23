import sqlite3 as sqlite

db = sqlite.connect("banyol.db")

cur = db.cursor()

cur.execute("DROP TABLE IF EXISTS corpus_index")
cur.execute("CREATE TABLE corpus_index(id INTEGER PRIMARY KEY AUTOINCREMENT, word VARCHAR(50), \
            document_id INTEGER, FOREIGN KEY(document_id) REFERENCES berkas(id))")

db.commit()
