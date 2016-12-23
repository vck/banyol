import numpy as np
import records
import sqlite3 as sqlite
from flask import (
    Flask,
    render_template,
    request,
    redirect,
    url_for
)



db2 = sqlite.connect("banyol.db", check_same_thread=False)
cur = db2.cursor()

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

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    return render_template('index.html')


@app.route("/search", methods=["POST"])
def search():
    query = request.form["text"].lower()
    if query:
        documents = cur.execute("SELECT * FROM corpora").fetchall()
        print "checking query: {0} on documents with length {1}".format(query, len(documents))
        result = []
        for doc in documents:
            a, b = vsm3(query, doc[1])
            dot = np.dot(a, b)
            if dot > 0:
                res = (doc[1], cur.execute("SELECT filename FROM berkas WHERE id={}".format(doc[0])).fetchall()[0][0])
        if result:
            print "found match: {}".format(len(result))
            return render_template('index.html', result=result)
        return redirect(url_for("index"))


if __name__ == "__main__":
    app.debug = True
    app.run()
