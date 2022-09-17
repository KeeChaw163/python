import numpy as np
from flask import Flask, make_response, render_template, request, redirect, url_for

app = Flask(__name__)

app.config.from_pyfile('settings.py')

# ===============Hello--KeeChaw===============
@app.route('/')
def hello():
    return '<h2 style="text-align: center;">欢迎来到KeeChaw</h2>'

# ===============index===============
@app.route("/index")
def index():

    students = np.array([
        {'studentname': '李辉港', 'pscore': '70', 'qscore': '86'},
        {'studentname': '张鹏', 'pscore': '83', 'qscore': '73'},
        {'studentname': '周灿', 'pscore': '65', 'qscore': '65'},
        {'studentname': '车彦荣', 'pscore': '70', 'qscore': '68'},
        {'studentname': '杨旭东', 'pscore': '60', 'qscore': '55'},
        {'studentname': '雷默强', 'pscore': '75', 'qscore': '66'}
    ])

    return render_template("homeWork3.html", students=students)

# ===============主函数、程序入口===============
if __name__ == '__main__':
    # print(app.config)
    app.run(port=8080)