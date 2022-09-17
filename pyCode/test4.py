import json

from flask import Flask, make_response, render_template, request, redirect, url_for

app = Flask(__name__)

app.config.from_pyfile('settings.py')

@app.route("/index")
def index():
    usern = "KeeChaw"
    num = [1,2,3]
    user = {'un':'keechaw','pwd':'123'}
    return render_template('index1.html',usern=usern,num=num,user=user)

# ===============主函数、程序入口===============
if __name__ == '__main__':
    # print(app.config)
    app.run(port=8080)