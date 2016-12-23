import sqlite3 as sqlite

db = sqlite.connect("banyol.db")
cur = db.cursor()
corpora = cur.execute("SELECT * FROM corpora;").fetchall()


stopwords = ["and", "if", "or", "with"]


for i in range(len(corpora)):
        if corpus not in stopwords:
    for corpus in corpora[i][1].split(" "):
            cur.execute("""
            INSERT INTO corpus_index(word, document_id) VALUES ("{0}", "{1}")""".format(corpus, corpora[i][0]))

db.commit()
