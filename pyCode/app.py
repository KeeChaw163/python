import json

from flask import Flask, make_response, render_template, request, redirect, url_for

app = Flask(__name__)

app.config.from_pyfile('settings.py')

users = []


# ===============HelloWorld===============
@app.route('/')
def hello():
    return '<h2 style="text-align: center;">欢迎来到KeeChaw</h2>'

# ===============GET获取===============
@app.route('/register0')
def register0():
    # print(request.args)
    # print(request.args['username'])
    # print(request.args["pwd"])
    user = request.args.get('username')
    pwd = request.args.get('pwd')
    user0 = {'username': user, 'pwd': pwd}
    users.append(user0)
    print(users)
    return render_template("register.html")  # 渲染模板


# ===============POST获取===============
@app.route('/post_register', methods=['GET', 'POST'])
def post_register():
    # print(request.form)
    # print(request.args['username'])
    # print(request.args["pwd"])
    user1 = request.form.get('username1')
    pwd1 = request.form.get('pwd1')
    user = {'username': user1, 'pwd': pwd1}
    users.append(user)
    print(users)
    return render_template("post_regist.html")  # 渲染模板

# ===============首页===============
@app.route('/index')
def index():
    return render_template("index.html")  # 渲染模板

# ===============注册===============
@app.route('/register', methods=['GET', 'POST'])
def register():
    # print(request.form)
    # print(request.args['username'])
    # print(request.args["pwd"])
    if request.method == 'POST':
        user = request.form.get('username1')
        pwd = request.form.get('pwd1')
        repwd = request.form.get('repwd1')
        user = {'username': user, 'pwd': pwd}
        if pwd == repwd:
            if user and pwd and repwd != None:
                users.append(user)
                print('=====注册成功=====')
                print('users内数据：{}'.format(users))
                return redirect(url_for('login'))
            else:
                return '<h2>注册失败，用户名和密码不能为空！！！</h2>'
        else:
            return '<h2>注册失败，两次密码输入不正确！！！</h2>'
    return render_template("r1.html")  # 渲染模板


# ===============登录===============
@app.route('/login', methods=['GET', 'POST'])
def login():
    # print(request.form)
    # print(request.args['username'])
    # print(request.args["pwd"])
    if request.method == 'POST':
        user1 = request.form.get('username2')
        pwd1 = request.form.get('pwd2')
        user = {'username': user1, 'pwd': pwd1}
        if user in users:
            print('=====登录成功=====')
            return redirect(url_for('index'))
        else:
            return '<h2>登录失败，账号或密码错误！！！</h2>'
    return render_template("login.html")  # 渲染模板


# ===============展示===============
@app.route('/show')
def show():
    str_user = json.dumps(users)
    return str_user


# ===============主函数、程序入口===============
if __name__ == '__main__':
    # print(app.config)
    app.run(port=8080)
