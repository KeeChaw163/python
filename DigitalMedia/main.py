"""
   KeeChaw
   2022.09.16

"""

import requests
import json
import pymysql

url = "https://api.inews.qq.com/newsqa/v1/query/inner/publish/modules/list?modules=localCityNCOVDataList,diseaseh5Shelf"

conn = pymysql.connect(host='localhost', user='root', passwd='root', port=3306, database='race', charset='utf8')
cur = conn.cursor()
sql = "CREATE TABLE covid19(" \
      "province VARCHAR(255)," \
      "nowConfirm VARCHAR(255)," \
      "dead  VARCHAR(255)," \
      "heal VARCHAR(255))"
cur.execute(sql)
response = requests.post(url)
json_data = response.json()['data']
# print(type(json_data))
json_data = json.loads(json.dumps(json_data),strict=False)
print(json_data)
china_data = json_data['diseaseh5Shelf']['areaTree'][0]['children']

for i in china_data:
    # 地区名称
    province = i['name']
    # 新增确认
    nowConfirm = i['total']['confirm']
    # 死亡人数
    dead = i['total']['dead']
    # 治愈人数
    heal = i['total']['heal']

    cur.execute('insert into covid19(province,nowConfirm,dead,heal)'
                ' values (%s,%s,%s,%s)',(province,nowConfirm,dead,heal))


    conn.commit()




