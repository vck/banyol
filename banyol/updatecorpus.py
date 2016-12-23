#!/usr/bin/env python
# coding=utf-8

import re
import records

DB_NAME = "banyol.db"

db = records.Database("sqlite:///"+DB_NAME)

regex = re.compile("[^w']|[_, -]")


def normalizer(w):
    if w.endswith("pdf"):
        return w.split("/")[-1].strip(".pdf").lower()

def main():
    doc = db.query("SELECT * FROM berkas")
    corpora = doc.all()
    cleaned_corpora = [normalizer(w) for w in corpora]
    for corpus in corpora:



if __name__ == "__main__":
    main()
