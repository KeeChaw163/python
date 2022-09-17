"""
   KeeChaw
   2022.09.16

"""
from flask import Flask
from flask import render_template
import pymysql


app = Flask(__name__)

conn = pymysql.connect(
    host='localhost',
    user='root',
    password='root',
    db = 'race',
    charset='utf8')

@app.route('/')
def hello_world():
    cur = conn.cursor()

    sql = "select * from covid19"
    cur.execute(sql)
    content = cur.fetchall()
    print(content)

    sql = "show fields from covid19"
    cur.execute(sql)
    labels = cur.fetchall()
    labels = [l[0] for l in labels]
    print(labels)

    return render_template("index.html",content=content,labels=labels)

if __name__== '__main__':
    app.run(port=8888)
