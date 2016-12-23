import numpy as np
import records
import sqlite3 as sqlite

db = records.Database("sqlite:///banyol.db")

def vsm3(w, x):
    a = []
    b = []


    for i in w.split():
        if i in x.split():
            a.append(1)
        else:
            a.append(0)

    for j in x.split():
        if j in w.split():
            b.append(1)
        else:
            b.append(0)

    if len(a) > len(b):
        tetha = len(a) - len(b)
        for i in range(tetha):
            lenb = len(b)
            b.insert(lenb, 0)
        return a, b

    elif len(a) < len(b):
        tetha = len(b) - len(a)
        for i in range(tetha):
            lena = len(a)
            a.insert(lena, 0)
        return a, b

    return a, b

def search():
    query = raw_input(">> ")
    documents = db.query("SELECT * FROM corpora")
    for doc in documents:
        a, b = vsm3(query, doc.corpus)
        dot = np.dot(a, b)
        if dot > 0:
            print "query: {}".format(query)
            print "corpus: {}".format(doc.corpus)
            print db.query("SELECT filename FROM berkas WHERE id={}".format(doc.berkasid)).all()[0].filename

if __name__ == '__main__':
    while True:
        search()
