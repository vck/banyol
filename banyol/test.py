import sqlite3 as sqlite

db = sqlite.connect("banyol.db")
cur = db.cursor()

while True:
    query = raw_input(">> ")
    for word in query.lower().split():
        doc_id = cur.execute("SELECT document_id FROM corpus_index WHERE word='{0}'".format(word)).fetchall()
        if len(doc_id)>0:
            for id in doc_id:
                document = cur.execute("SELECT filename FROM berkas WHERE id={}".format(id[0])).fetchall()
                print document
