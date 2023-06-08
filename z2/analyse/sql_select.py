"""
    @author: 欢乐干饭人小组
    @content: 查询MySQL数据-----连接数据库查取数据
    @time: 2023.05.09
"""

import json
import pymysql

class sql_select():
    conn = pymysql.connect(
        host='localhost',          # MySQL本地服务器
        user='root',               # 用户名
        password='root',           # 密码
        db='contest',           # 数据库名称
        charset='utf8')

    # 查询所有中国、兰州数据
    def select1(self, conn):
        cur = conn.cursor()

        sql = "SELECT * FROM popularpeoplesnew"
        cur.execute(sql)
        content = cur.fetchall()
        # print(type(content))

        content_list = (list(content))
        content_recording_list = []
        for i in content_list:
            content_recording_list.append(list(i))
            # print(content_recording_list)
        # new_content_recording_list = json.dumps(content_recording_list, ensure_ascii=False)
        print(type(content_recording_list))
        return content_recording_list

    # ech1数据
    def select2(self, conn):
        cur = conn.cursor()

        sql_2020 = "SELECT jingdian, xiaoliang FROM `popularattractions` LIMIT 200;"
        cur.execute(sql_2020)
        content_2020 = cur.fetchall()

        content_list_2020 = (list(content_2020))
        r_ech1 = []
        for i in content_list_2020:
            r_ech1.append(list(i))
        # print(content_recording_list)
        new_r_ech1 = json.dumps(r_ech1, ensure_ascii=False)
        return new_r_ech1

    # ech2数据
    def select3(self, conn):
        cur = conn.cursor()

        sql_gs = "SELECT jingdian, youhuijia, jiage FROM `popularattractions`  LIMIT 200;"
        cur.execute(sql_gs)
        content_gs = cur.fetchall()

        content_list_gs = (list(content_gs))
        content_recording_list_gs = []
        for i in content_list_gs:
            content_recording_list_gs.append(list(i))
        # print(content_recording_list)
        r_ech3 = json.dumps(content_recording_list_gs, ensure_ascii=False)
        return r_ech3

    # 查询ech3数据
    def select4(self, conn):
        cur = conn.cursor()

        sql_china = "SELECT * FROM `popularpeoples`;"
        cur.execute(sql_china)
        content_china = cur.fetchall()

        content_list_china = (list(content_china))
        content_recording_list_china = []
        for i in content_list_china:
            content_recording_list_china.append(list(i))
        # print(content_recording_list)
        r_ech3 = json.dumps(content_recording_list_china, ensure_ascii=False)
        return r_ech3

    # 查询ech4数据
    def select5(self, conn):
        cur = conn.cursor()

        sql_news = "SELECT * FROM `popularpeoples` WHERE citys='天水' OR citys='兰州' OR citys='西安' OR citys='淄博';"
        cur.execute(sql_news)
        content_news = cur.fetchall()

        content_list_news = (list(content_news))
        content_recording_list_news = []
        for i in content_list_news:
            content_recording_list_news.append(list(i))
        # print(content_recording_list)
        r_ech4 = json.dumps(content_recording_list_news, ensure_ascii=False)
        return r_ech4

    # 查询ech5数据
    def select6(self, conn):
        cur = conn.cursor()

        sql_news = "SELECT * FROM `popularattractions` ORDER BY xiaoliang DESC;"
        cur.execute(sql_news)
        content_news = cur.fetchall()

        content_list_news = (list(content_news))
        r_ech5 = []
        for i in content_list_news:
            r_ech5.append(list(i))
        # print(content_recording_list)
        # r_ech5 = json.dumps(content_recording_list_news, ensure_ascii=False)
        return r_ech5

    # 查询ech5数据
    def selecta1(self, conn):
        cur = conn.cursor()

        sql_news = "SELECT * FROM `popularattractions` ORDER BY xiaoliang DESC;"
        cur.execute(sql_news)
        content_news = cur.fetchall()

        content_list_news = (list(content_news))
        content_recording_list_news = []
        for i in content_list_news:
            content_recording_list_news.append(list(i))
        # print(content_recording_list)
        a1_ech1 = json.dumps(content_recording_list_news, ensure_ascii=False)
        return a1_ech1

    # 查询knn数据
    def selectknn(self, conn):
        cur = conn.cursor()

        sql_news = "SELECT * FROM `populartravelogues`;"
        cur.execute(sql_news)
        content_news = cur.fetchall()

        content_list_news = (list(content_news))
        knn_test = []
        for i in content_list_news:
            knn_test.append(list(i))
        # print(content_recording_list)
        # a1_ech1 = json.dumps(content_recording_list_news, ensure_ascii=False)
        return knn_test

    # 查询cech1数据
    def selectc1(self, conn):
        cur = conn.cursor()

        sql_news = "SELECT * FROM `popularpeoples` ORDER BY people_nums DESC;"
        cur.execute(sql_news)
        content_news = cur.fetchall()

        content_list_news = (list(content_news))
        content_recording_list_news = []
        for i in content_list_news:
            content_recording_list_news.append(list(i))
        # print(content_recording_list)
        c1_ech1 = json.dumps(content_recording_list_news, ensure_ascii=False)
        return c1_ech1

    # 查询五一数据
    def selectc2(self, conn):
        cur = conn.cursor()

        sql_news = "SELECT * FROM `populartravelogues` WHERE time LIKE '%05-01' ORDER BY days DESC;"
        cur.execute(sql_news)
        content_news = cur.fetchall()

        content_list_news = (list(content_news))
        c2_ech2 = []
        for i in content_list_news:
            c2_ech2.append(list(i))
        # print(content_recording_list)
        # c2_ech2 = json.dumps(content_recording_list_news, ensure_ascii=False)
        return c2_ech2