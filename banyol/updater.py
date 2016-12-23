#!/usr/bin/env python
# coding=utf-8

import sqlite3 as sqlite
import os

DIR = "/media/vickydasta/code/BOOKS"
INSERT_BERKAS_QUERY = """INSERT INTO berkas(filename) VALUES({0})"""
db = sqlite.connect("banyol.db")
cur = db.cursor()

def main():
    #db = records.Database("sqlite:///banyol.db")
    
    cur.execute("DROP TABLE IF EXISTS berkas")
    cur.execute("""CREATE TABLE berkas(id INTEGER PRIMARY KEY\
                    AUTOINCREMENT,
                    filename varchar(50))
                """)
    db.commit()

    for root, dir, files in os.walk(DIR, topdown=False):
        for file in files:
            berkas = os.path.join(root, file)
            print "updating: {0} to banyol.db".format(berkas)
            try:
                cur.execute("""INSERT INTO berkas(filename)\
                        VALUES("{}")""".format(berkas))
            except Exception as err:
                print "unable to insert. --> {}".format(err)

    db.commit()
    print "banyol.db updated..."
    db.close()
if __name__ == "__main__":
    main()
