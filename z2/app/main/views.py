from analyse import sql_select
from app import get_logger, get_config, db1
import math
from flask import render_template, redirect, url_for, flash, request, jsonify
from flask_login import login_required, current_user
from app import utils
from . import main
from app.models import Popularattractions
from analyse import logistic



logger = get_logger(__name__)
cfg = get_config()

# 根目录跳转
@main.route('/', methods=['GET'])
@login_required
def root():
    return redirect(url_for('main.index'))

# 首页
@main.route('/index', methods=['GET'])
@login_required
def index():
    ss = sql_select.sql_select()
    xx = ss.select1(ss.conn)
    r_ech1 = ss.select2(ss.conn)
    r_ech2 = ss.select3(ss.conn)
    r_ech3 = ss.select4(ss.conn)
    r_ech4 = ss.select5(ss.conn)
    return render_template('index.html', current_user=current_user, xx=xx, r_ech1=r_ech1, r_ech2=r_ech2, r_ech3=r_ech3, r_ech4=r_ech4)

#
@main.route('/menu1_submenu', methods=['GET', 'POST'])
@login_required
def getMenu1_submenu1():
    ss = sql_select.sql_select()
    aech1 = ss.selecta1(ss.conn)
    return render_template("menu1/submenu1.html", aech1=aech1)

@main.route('/menu1_recommend', methods=['post', 'get'])
@login_required
def getMenu1_recommend():
    ss = sql_select.sql_select()
    aech1 = ss.selecta1(ss.conn)

    month = request.form.get('recommend_content1')
    trip = request.form.get('recommend_content2')
    day = request.form.get('recommend_content3')

    test_x_in = [[month, trip, day]]
    lt = logistic.Logistic_tourism()
    city = lt.test(test_x_in)

    return render_template('menu1/recommend.html', city=city, aech1=aech1)

@main.route('/menu1_submenu2', methods=['GET', 'POST'])
@login_required
def getMenu1_submenu2():
    ss = sql_select.sql_select()
    ech5 = ss.select6(ss.conn)
    return render_template("menu1/submenu2.html", ech5=ech5)

@main.route('/menu1_search', methods=['post', 'get'])
@login_required
def getMenu1_search():
    content = request.form.get('in_content')
    if content is None:
        content = " "
    popularattractions = db1.session.query(Popularattractions.jingdian, Popularattractions.citys, Popularattractions.xiaoliang, Popularattractions.youhuijia, Popularattractions.jiage).filter(Popularattractions.citys.like("%"+content+"%")if content is not None else "").all()
    print(popularattractions)
    return render_template('menu1/search.html', popularattractions=popularattractions, content=content)

# 公共配置
@main.route('/common_data1', methods=['GET', 'POST'])
@login_required
def getData1():
    ss = sql_select.sql_select()
    c1_ech1 = ss.selectc1(ss.conn)
    c2_ech2 = ss.select3(ss.conn)

    return render_template("common/data1.html", c1_ech1=c1_ech1, c2_ech2=c2_ech2)

@main.route('/common_data2', methods=['GET', 'POST'])
@login_required
def getData2():
    ss = sql_select.sql_select()
    c2_ech2 = ss.selectc2(ss.conn)
    return render_template("common/data2.html", c2_ech2=c2_ech2)

