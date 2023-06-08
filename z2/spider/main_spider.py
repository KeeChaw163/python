"""
    @author: KeeChaw
    @content: 爬取数据-----各大旅游网站携程、去哪儿、飞猪、马蜂窝（数据来源）
    @time: 2023.05.09
"""

# pip install pymysql==1.0.2
# pip install selenium==2.48.0

import math
import re, csv
import urllib
import pandas as pd
import pymysql
import requests
from bs4 import BeautifulSoup
from lxml import etree
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import os

# 去哪儿网
class spiders_province_people_area(object):

    # 模仿浏览器点击
    def imitate_click(self):
        dr = webdriver.Chrome()
        dr.get("https://www.baidu.com/")
        print("--------进入百度---------")
        time.sleep(2)
        dr.save_screenshot("results/Screenshot/img1.png")
        # 通过链id定位页面元素
        print("--------输入关键字(去哪儿网)---------")
        dr.find_element_by_id("kw").send_keys(u"去哪儿网")
        print("--------点击(百度一下)---------")
        dr.find_element_by_id("su").click()
        time.sleep(2)
        dr.save_screenshot("results/Screenshot/img2.png")
        # 通过链接文本定位页面元素
        print("--------点击进入(去哪儿网)---------")
        dr.find_element_by_link_text("去哪儿网").click()
        # 获取当前窗口的句柄
        handles = dr.window_handles
        # 切换至新打开的标签
        dr.switch_to.window(handles[1])
        time.sleep(5)
        dr.save_screenshot("results/Screenshot/img3.png")
        print("--------点击进入(攻略)---------")
        select = dr.find_element_by_xpath("//li[@class='qheader_gonglve']/a/span/b")
        # 修改为执行脚本
        dr.execute_script("arguments[0].click()", select)
        # 获取当前窗口的句柄
        handles = dr.window_handles
        # 切换至新打开的标签
        dr.switch_to.window(handles[1])
        time.sleep(2)
        dr.save_screenshot("results/Screenshot/img4.png")
        print("--------点击(功略库)---------")
        dr.find_element_by_xpath("//ul[@class='q_header_sub_menu_l']/li[2]/a").click()
        time.sleep(2)
        dr.save_screenshot("results/Screenshot/img5.png")
        # base_url = dr.page_source
        base_url = dr.current_url
        dr.close()
        dr.quit()
        print(base_url)
        return base_url

    # 爬取页数输入
    def input_page(self):
        begin_page = int(input("请输入热门游记起始页数:"))
        end_page = int(input("请输入热门游记终止页数:"))
        page_list = [begin_page, end_page]
        return page_list

    # 发送爬取网页的请求
    def load_page(self, base_url, page_list):
        # user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 Edg/113.0.1774.50"
        headers = {
            'authority': 'travel.qunar.com',
            'cookie': 'QN1=00008580306c5086c7606cbe; QN300=s%3Dbing; QN99=1786; QunarGlobal=10.68.20.162_-751f5d42_18800435bd4_49fa|1683641068625; QN205=s%3Dbing; QN277=s%3Dbing; _i=VInJOmZ530RqBtT1Y1qRarcHNucq; QN601=fcfaa90fb6fcdd76411523840bfac2b7; QN48=d39d1b05-cfee-4c6d-8413-fb712821964b; QN269=6A10C600EE7211EDAC50FA163E55E8BB; fid=c9fb1276-6b98-4c13-ae5b-07ce6e2b6397; ariaDefaultTheme=null; viewdist=299914-1; uld=1-299914-1-1684150999; qunar-assist={%22version%22:%2220211215173359.925%22%2C%22show%22:false%2C%22audio%22:false%2C%22speed%22:%22middle%22%2C%22zomm%22:1%2C%22cursor%22:false%2C%22pointer%22:false%2C%22bigtext%22:false%2C%22overead%22:false%2C%22readscreen%22:false%2C%22theme%22:%22default%22}; csrfToken=BLtxPcJG2LEq3izAdPvYGUYl4frJxgrV; _vi=D4gYXep3fQl1GyaKVh2dZuWy-qbUBscDigO-31r_aPV0-aUu2Fux2f9ZDS8QQ36bsKT7e3-JJIxBZZsBaIt39j7gyT6SdE3knxaSHHBNMzJar14Lj4Tx7zPFTJlDPMHPWBi_sYiTMWWaUwDOO1xh_f3NzgCIObz8hrXKw_cU35LA; QN163=0; JSESSIONID=F1A05C43402ED3154364F45C821DCAAE; Hm_lvt_c56a2b5278263aa647778d304009eafc=1684158202,1684225259,1684686700,1684841413; Hm_lpvt_c56a2b5278263aa647778d304009eafc=1684841413; QN271=105621ca-fd13-46ff-8ffc-e588a6953ef3; QN267=035179201080736e14',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 Edg/113.0.1774.50'
        }
        htmls = []
        split_url_list = base_url.split("?")
        for page in range(page_list[0], page_list[1]+1):
            url = split_url_list[0]+"?"+"page="+str(page)+"&"+split_url_list[1]
            print(url)
            request = urllib.request.Request(url, headers=headers)
            # 获取每页HTML源代码字符串
            response = urllib.request.urlopen(request)
            html = response.read().decode("utf-8")
            htmls.append(html)
        return htmls

    # 解析网页数据
    def parse_page(self, htmls):

        items = []

        for html in htmls:

            root = etree.HTML(html)

            nums = root.xpath("//ul[@class='b_strategy_list ']/li/p[@class='user_info']/span/span[@class='user_name']/a[1]")

            for i in range(1, len(nums)+1):
                # titles = root.xpath("//ul[@class='b_strategy_list ']/li[{}]/h2/a/text()".format(i))
                authors = root.xpath("//ul[@class='b_strategy_list ']/li[{}]/p[@class='user_info']/span/span[@class='user_name']/a[1]/text()".format(i))
                begin_times = root.xpath("//ul[@class='b_strategy_list ']/li[{}]/p[@class='user_info']/span/span[@class='date']/text()".format(i))
                days_times = root.xpath("//ul[@class='b_strategy_list ']/li[{}]/p[@class='user_info']/span/span[@class='days']/text()".format(i))
                citys = root.xpath("//ul[@class='b_strategy_list ']/li[{}]/p[@class='places'][1]/text()".format(i))
                road_citys = root.xpath("//ul[@class='b_strategy_list ']/li[{}]/p[@class='places'][2]/text()".format(i))
                photo_num = root.xpath("//ul[@class='b_strategy_list ']/li[{}]/p[@class='user_info']/span/span[@class='photo_nums']/text()".format(i))
                trips = root.xpath("//ul[@class='b_strategy_list ']/li[{}]/p[@class='user_info']/span/span[@class='trip']/text()".format(i))

                item=[]
                # try:
                #     item.append(titles[0])
                # except IndexError:
                #     item.append(' ')
                try:
                    item.append(authors[0])
                except IndexError:
                    item.append(' ')
                try:
                    item.append(begin_times[0])
                except IndexError:
                    item.append('  ')
                try:
                    item.append(days_times[0])
                except IndexError:
                    item.append('  ')
                try:
                    if len(citys) == 0:
                        item.append('  ')
                    else:
                        item.append(citys)
                except IndexError:
                    item.append('  ')
                try:
                    if len(road_citys) == 0:
                        item.append('  ')
                    else:
                        item.append(road_citys)
                except IndexError:
                    item.append('  ')
                try:
                    item.append(photo_num[0])
                except IndexError:
                    item.append('  ')
                try:
                    item.append(trips[0])
                except IndexError:
                    item.append('  ')
                items.append(item)
        return items

    # 数据预处理
    def data_pretreatment(self, new_items, item_row):
        new_pd_items = pd.DataFrame(columns=item_row, data=new_items)
        chufa = []
        days = []
        citys = []
        road_citys = []
        photos = []
        for i in new_pd_items['出发日期']:
            i = i.replace(' 出发', '')
            chufa.append(i)
        for i in new_pd_items['历经时长']:
            i = i.replace('共', '')
            i = i.replace('天', '')
            days.append(i)
        for i in new_pd_items['城市']:
            i = " ".join(i)
            i = i.replace("'", '')
            i = i.replace('途经：', '')
            i = i.replace('，', ' ')
            citys.append(i)
        for i in new_pd_items['景点']:
            i = " ".join(i)
            i = i.replace("'", '')
            i = i.replace('行程：', '')
            i = i.replace('，', ' ')
            road_citys.append(i)
        for i in new_pd_items['拍摄数量']:
            i = i.replace('张照片', '')
            photos.append(i)
        new_pd_items['出发日期'] = chufa
        new_pd_items['历经时长'] = days
        new_pd_items['城市'] = citys
        new_pd_items['景点'] = road_citys
        new_pd_items['拍摄数量'] = photos
        #         print(new_pd_items)
        return new_pd_items

    # 将数据保存在csv文件中
    def save_file(self, new_pd_items):
        new_pd_items.to_csv("./results/result/PopularTravelogues.csv", encoding='utf-8-sig')
        print("数据已解析，并保存在" + "D:/Code/PythonCode/z2/spider/results/result路径下的PopularTravelogues.csv文件中，请前往查看！")

    # 将数据保存在MySQL数据库中
    def save_mysql(self, items):
        print("---------开始连接MySQL---------")
        db = pymysql.connect(host='localhost', user='root', password='root', port=3306, db='contest')
        cur = db.cursor()
        print('---------开始创建表---------')
        sql_drop = "DROP TABLE IF EXISTS PopularTravelogues;"
        cur.execute(sql_drop)
        sql = 'CREATE TABLE PopularTravelogues(name VARCHAR(255), time DATE, days INT, citys VARCHAR(255), road_city VARCHAR(255), photos INT, trips VARCHAR(255))  CHARSET=utf8 COLLATE utf8_general_ci;'
        cur.execute(sql)
        print("---------PopularTravelogues表创建成功---------")

        for data in items.values:
            data = data.tolist()
            # print(data)
            # print(type(data))
            sql = 'insert into PopularTravelogues(name, time, days, citys, road_city, photos, trips)values(%s,%s,%s,%s,%s,%s,%s)'
            try:
                cur.execute(sql, data)
            except TypeError:
                print("TypeError!!!!")
                pass
        print("---------插入成功---------")
        cur.close()
        db.commit()
        db.close()
        return "数据已解析，并保存在MySQL数据库contest下的PopularTravelogues表中，请前往查看！"

# 马蜂窝网
class spider_hot_city():

    # 爬取数据
    def hot_city_tourist(self):
        city_list = []
        tourist_list = []
        data = []

        with open('./text/全国城市.txt', 'r', encoding='utf-8') as f:
            search = f.read().strip()  # 每个字符作为列表的一项，包括换行符
            search_list = search.split('\n')  # 以换行符作为分隔重新构建列表

        for search_city in search_list:
            print(search_city)
            search_city = search_city.replace('市', '')
            url = 'https://www.mafengwo.cn/search/q.php?q=' + str(search_city)
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 '
                              'Safari/537.36 Edg/109.0.1518.61 ',
                'Host': 'www.mafengwo.cn',
                'Cookie': '__jsluid_s=d3db61a0e5b7d2f3ebe46fc242b4d50c; mfw_uuid=63ca952a-fc7e-9255-dc7b-fc67323dcc47; '
                          'oad_n=a:3:{s:3:"oid";i:1029;s:2:"dm";s:15:"www.mafengwo.cn";s:2:"ft";s:19:"2023-01-20+21:20:42";}; '
                          '__mfwc=direct; uva=s:92:"a:3:{s:2:"lt";i:1674220844;s:10:"last_refer";s:24:"https://www.mafengwo.cn'
                          '/";s:5:"rhost";N;}";; __mfwurd=a:3:{'
                          's:6:"f_time";i:1674220844;s:9:"f_rdomain";s:15:"www.mafengwo.cn";s:6:"f_host";s:3:"www";}; '
                          '__mfwuuid=63ca952a-fc7e-9255-dc7b-fc67323dcc47; __jsluid_h=3e9a93c05a720da6489c8c6194e80523; '
                          '__omc_chl=; __omc_r=; PHPSESSID=m251pri7l2dbdvqvojatdrse75; __mfwlv=1674614862; __mfwvn=2; '
                          'Hm_lvt_8288b2ed37e5bc9b4c9f7008798d2de0=1674220843,1674614863; bottom_ad_status=0; '
                          '__mfwb=c4818c8a23f3.1.direct; __mfwa=1674220841568.75085.3.1674614862237.1674618443150; '
                          '__mfwlt=1674618443; Hm_lpvt_8288b2ed37e5bc9b4c9f7008798d2de0=1674618444 ',
                'sec-ch-ua': '"Not_A Brand";v="99", "Microsoft Edge";v="109", "Chromium";v="109"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'Sec-Fetch-Dest': 'document',
                'Sec-Fetch-Mode': 'navigate',
                'Sec-Fetch-Site': 'none',
                'Sec-Fetch-User': '?1',
                'Upgrade-Insecure-Requests': '1',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,'
                          'application/signed-exchange;v=b3;q=0.9',
                'Accept-Encoding': 'gzip, deflate, br',
                'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
                'Cache-Control': 'max-age=0',
                'Connection': 'keep-alive'
            }

            page_text = requests.get(url=url, headers=headers).content
            soup = BeautifulSoup(page_text, 'lxml')
            p = re.compile(r'>.*?<')
            city = str(soup.select('.mfw-search-main > div > div > .search-mdd-wrap > a > div > .title '))
            tourist = str(soup.select('.mfw-search-main > div > div > .search-mdd-wrap > a > div > .content > b > font'))

            # 正则返回的是一个list类型，需要取出其中元素进行操作
            try:
                city = p.findall(city)[0]
                tourist = p.findall(tourist)[0]
            except IndexError as e:
                print(e)
                pass
            print(city, ' ', tourist)

            city_list.append(city.replace('>', '').replace('<', ''))
            tourist_list.append(tourist.replace('>', '').replace('<', ''))

        for i in range(len(city_list)):
            data.append([city_list[i], tourist_list[i]])

        # print(data)
        return data

    # 保存csv
    def save_csv(self, head, data):
        new_data = pd.DataFrame(columns=head, data=data)
        new_data.to_csv("./results/result/PopularPeoples.csv", encoding='utf-8-sig')
        print('PopularPeoples.csv文件，保存成功！')

    # 将数据保存在MySQL数据库中
    def save_mysql(self, items):
        print("---------开始连接MySQL---------")
        db = pymysql.connect(host='localhost', user='root', password='root', port=3306, db='contest')
        cur = db.cursor()
        print('---------开始创建表---------')
        sql_drop = "DROP TABLE IF EXISTS PopularPeoples;"
        cur.execute(sql_drop)
        sql = 'CREATE TABLE PopularPeoples(citys VARCHAR(255), people_nums MEDIUMINT)  CHARSET=utf8 COLLATE utf8_general_ci;'
        cur.execute(sql)
        print("---------PopularPeoples表创建成功---------")
        for data in items:
            # data = data.tolist()
            sql = 'insert into PopularPeoples(citys, people_nums)values(%s,%s)'
            try:
                cur.execute(sql, data)
            except Exception as e:
                print(e)
                pass
        print("---------插入成功---------")
        cur.close()
        db.commit()
        db.close()
        return "数据已解析，并保存在MySQL数据库contest下的PopularPeoples表中，请前往查看！"

# 携程网
class spider_city_want():

    popular_city = ['beijing1', 'shanghai2', 'chengdu104', 'guangzhou152', 'hangzhou14',
                    'chongqing158', 'shenzhen26', 'suzhou11', 'nanjing9', 'xian7',
                    'xiamen21', 'tianjin154', 'wuhan145', 'jiaxing272', 'sanya61',
                    'kunming29', 'changsha148', 'wuxi10', 'jilin267', 'foshan207',
                    'lijiang32', 'dali1445616', 'qingdao5', 'zhengzhou157', 'zibo536']
    city_name = ['北京', '上海', '成都', '广州', '杭州',
                 '重庆', '深圳', '苏州', '南京', '西安',
                 '厦门', '天津', '武汉', '嘉兴', '三亚',
                 '昆明', '长沙', '无锡', '吉林', '佛山',
                 '丽江', '大理', '青岛', '郑州', '淄博']
    # popular_city = ['beijing1', 'shanghai2', 'chengdu104']
    # city_name = ['北京', '上海', '成都']
    headers = {"authority": "you.ctrip.com",
               "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
               "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
               "cache-control": "no-cache",
               "pragma": "no-cache",
               "sec-ch-ua": "^\\^Not_A",
               "sec-ch-ua-mobile": "?0",
               "sec-ch-ua-platform": "^\\^Windows^^",
               "sec-fetch-dest": "document",
               "sec-fetch-mode": "navigate",
               "sec-fetch-site": "same-origin",
               "sec-fetch-user": "?1",
               "upgrade-insecure-requests": "1",
               "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 Edg/109.0.1518.69"}

    # 中国 兰州
    def parse_data(self):
        popular_city = ['china110000', 'lanzhou231']
        city_name = ['中国', '兰州']
        want_to, have_gone, data = [], [], []
        reflect = 0
        bro = webdriver.Chrome()

        for city in popular_city:
            print(city)
            url = 'https://you.ctrip.com/travels/' + city + '.html'
            bro.get(url)
            # 获取浏览器当前页面的源码数据
            page_text = bro.page_source
            soup = BeautifulSoup(page_text, "lxml")
            will = soup.select("#emWantValueID")[0].string
            went = soup.select("#emWentValueID")[0].string
            want_to.append(will)
            have_gone.append(went)
            name = city_name[reflect]
            reflect += 1
            data.append([name, will, went])
        bro.quit()
        pd.DataFrame(columns=['城市', '想去的人', '去过的人']).to_csv('./results/result/PopularPeoplesNew.csv', encoding='utf-8-sig')
        print("---------开始连接MySQL---------")
        db = pymysql.connect(host='localhost', user='root', password='root', port=3306, db='contest')
        cur = db.cursor()
        print('---------开始创建表---------')
        sql_drop = "DROP TABLE IF EXISTS PopularPeoplesNew;"
        cur.execute(sql_drop)
        sql = 'CREATE TABLE PopularPeoplesNew(citys VARCHAR(255), will_go MEDIUMINT, went_go MEDIUMINT)  CHARSET=utf8 COLLATE utf8_general_ci;'
        cur.execute(sql)
        print("---------PopularPeoplesNew表创建成功---------")
        for da in data:
            # data = data.tolist()
            sql = 'insert into PopularPeoplesNew(citys, will_go, went_go)values(%s,%s,%s)'
            try:
                cur.execute(sql, da)
            except TypeError:
                print("TypeError!!!!")
                pass
        print("---------插入成功---------")
        cur.close()
        db.commit()
        db.close()
        return "数据已解析，并保存在MySQL数据库contest下的PopularPeoplesNew表中，请前往查看！"

    # 各城市、各季度
    def getdata(self, popular_city, city_name, headers):
        name_list = []  # 游记名称
        date_list = []  # 出游日期
        time_list = []  # 出游时长
        cost_list = []  # 旅行花费
        whom_list = []  # 和谁出游
        read_list = []  # 浏览
        like_list = []  # 喜欢
        chat_list = []  # 回复
        newdata = []
        for i in range(len(city_name)):
            for m in range(1, 5):
                name_list.clear()
                date_list.clear()
                time_list.clear()
                cost_list.clear()
                whom_list.clear()
                read_list.clear()
                like_list.clear()
                chat_list.clear()

                url = 'https://you.ctrip.com/travels/beijing1/t2-m'+str(m)+'.html'
                page_text = requests.get(url=url, headers=headers, timeout=(100, 100))
                html = page_text.content.decode('utf-8', 'ignore')
                # soup = BeautifulSoup(html, 'lxml')

                # page = int(soup.find_all('b', class_="numpage")[0].text)-1

                for p in range(10):
                    print(city_name[i]+str(m)+':Page'+str(p)+'/'+str(25))

                    url = 'https://you.ctrip.com/travels/' + popular_city[i] + '/t2-p' + str(p)+ '-m' +str(m)+ '.html'
                    page_text = requests.get(url=url, headers=headers, timeout=(100, 100))
                    html = page_text.content.decode('utf-8', 'ignore')
                    soup = BeautifulSoup(html, 'lxml')

                    name_text = soup.find_all('dt', class_="ellipsis")
                    tag_text = soup.find_all('span', class_="tips_a")
                    read_text = soup.find_all('i', class_="numview")
                    like_text = soup.find_all('i', class_="want")
                    chat_text = soup.find_all('i', class_="numreply")

                    r = len(name_text)
                    for j in range(r):
                        tag = tag_text[j].text
                        time = re.search(r'.天', str(tag))
                        if time is None:
                            time = ''
                        else:
                            time = time.group()
                        date = re.search(r'20\d\d-\d\d-\d\d \d\d:\d\d:\d\d', str(tag))
                        if date is None:
                            date = ''
                        else:
                            date = date.group()
                        cost = re.search(r'￥\d*', str(tag))
                        if cost is None:
                            cost = ''
                        else:
                            cost = cost.group()
                        if cost == '￥1':        # 稍微清洗一下广告，大约能洗掉25%
                            continue
                        whom = re.search(r'亲子|和父母|和朋友|一个人|夫妻|情侣', str(tag))
                        if whom is None:
                            whom = ''
                        else:
                            whom = whom.group()

                        name = name_text[j].text
                        read = read_text[j].text
                        like = like_text[j].text
                        chat = chat_text[j].text

                        name_list.append(name.encode('gbk', 'ignore').decode('gbk'))
                        date_list.append(date.encode('gbk', 'ignore').decode('gbk'))
                        time_list.append(time.encode('gbk', 'ignore').decode('gbk'))
                        cost_list.append(cost.encode('gbk', 'ignore').decode('gbk'))
                        whom_list.append(whom.encode('gbk', 'ignore').decode('gbk'))
                        read_list.append(read.encode('gbk', 'ignore').decode('gbk'))
                        like_list.append(like.encode('gbk', 'ignore').decode('gbk'))
                        chat_list.append(chat.encode('gbk', 'ignore').decode('gbk'))

                        r = len(name_list)
                        for j in range(r):
                            time_list[j] = time_list[j].replace('天', '')
                            cost_list[j] = cost_list[j].replace('￥', '')
                            date_list[j] = date_list[j].replace(' 00:00:00', '')
                            data = [city_name[i], name_list[j], date_list[j], time_list[j], cost_list[j],
                                whom_list[j], read_list[j], like_list[j], chat_list[j], m]
                            newdata.append(data)
        head = ['城市', '游记名称', '出游日期', '出游时长', '旅行花费', '和谁出游', '浏览', '喜欢', '回复', '季度']
        newdata1 = pd.DataFrame(columns=head, data=newdata)
        newdata1.to_csv('./results/result/PopularMain.csv', encoding='utf-8-sig')
        return newdata

    # 将数据保存在MySQL数据库中
    def save_mysql(self, items):
        print("---------开始连接MySQL---------")
        db = pymysql.connect(host='localhost', user='root', password='root', port=3306, db='contest')
        cur = db.cursor()
        print('---------开始创建表---------')
        sql_drop = "DROP TABLE IF EXISTS PopularMain;"
        cur.execute(sql_drop)
        sql = 'CREATE TABLE PopularMain(citys VARCHAR(255), name VARCHAR(255), times DATE, days CHAR(12), mnoey CHAR(12), trips VARCHAR(255), liulans CHAR(12), likes VARCHAR(12), huifu VARCHAR(12), jidu CHAR(4))  CHARSET=utf8 COLLATE utf8_general_ci;'
        cur.execute(sql)
        print("---------PopularMain表创建成功---------")
        for data in items:
            # data = data.tolist()
            sql = 'insert into PopularMain(citys, name, times, days, mnoey, trips, liulans, likes, huifu, jidu)values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
            try:
                cur.execute(sql, data)
            except Exception as e:
                print(e)
                pass
        print("---------插入成功---------")
        cur.close()
        db.commit()
        db.close()
        return "数据已解析，并保存在MySQL数据库contest下的PopularMain表中，请前往查看！"

# 飞猪网
class spider_city_money():

    # 爬取数据
    def parse_page(self):
        options = Options()
        options.add_argument('--disable-gpu')  # 不使用 gpu
        prefs = {"profile.managed_default_content_settings.images": 2}  # 不显示图片
        options.add_experimental_option("prefs", prefs)
        driver = webdriver.Chrome()

        url = 'http://s.fliggy.com/scenic/list.htm?q=广州'
        driver.get(url)
        time.sleep(2)
        data = []

        try:
            # 获取页数
            next_num = driver.find_element(By.XPATH, "//a[@class='pi-pagination-num'][3]").text
        except Exception as e:
            # 处理只有一页的情况
            next_num = 1
            print(e)

        # for i in range(0, int(next_num)):
        for i in range(0, 100):
            links = driver.find_elements(By.XPATH, "//a[@class='pi-btn pi-btn-primary']")

            for link in links:
                try:
                    print(link.get_attribute("href"))
                    res = requests.get(link.get_attribute("href"), timeout=10)
                    soup = BeautifulSoup(res.text, 'lxml')
                    name = soup.find('h3', {'class': 'scenic-tit'}).get_text().strip()
                    city = soup.find('span', {'class': 'scenic-subtit'}).get_text().strip()
                    sell_count = soup.find('dl', {'class': 'sell-count'}).find('dd').find('em').get_text().strip()
                    scenic_price = soup.find('span', {'class': 'pi-price-lgt'}).get_text().strip()
                    price = soup.find('div', {'class': 'right-area'}).find('span', {'class': 'pi-price'}).get_text().strip()
                    price = price.replace('¥', '')
                    scenic_price = scenic_price.replace('¥', '')
                    row = [name, city, sell_count, scenic_price, price]
                    data.append(row)
                except Exception as e:
                    print(e)
            try:
                # 点击下一页
                driver.find_element(By.CLASS_NAME, 'pi-pagination-next').click()
            except Exception as e:
                print(e)

            # time.sleep(3)

        # 退出浏览器
        driver.quit()
        return data

    # 保存csv
    def save_csv(self, head, data):
        newData = pd.DataFrame(columns=head, data=data)
        newData.to_csv("./results/result/PopularAttractions.csv", encoding='utf-8-sig')

    # 将数据保存在MySQL数据库中
    def save_mysql(self, items):
        print("---------开始连接MySQL---------")
        db = pymysql.connect(host='localhost', user='root', password='root', port=3306, db='contest')
        cur = db.cursor()
        print('---------开始创建表---------')
        sql_drop = "DROP TABLE IF EXISTS PopularAttractions;"
        cur.execute(sql_drop)
        sql = 'CREATE TABLE PopularAttractions(jingdian VARCHAR(255), citys VARCHAR(255), xiaoliang INT, youhuijia FLOAT, jiage FLOAT)  CHARSET=utf8 COLLATE utf8_general_ci;'
        cur.execute(sql)
        print("---------PopularAttractions表创建成功---------")
        for data in items:
            # data = data.tolist()
            sql = 'insert into PopularAttractions(jingdian, citys , xiaoliang, youhuijia, jiage)values(%s,%s,%s,%s,%s)'
            try:
                cur.execute(sql, data)
            except TypeError:
                print("TypeError!!!!")
                pass
        print("---------插入成功---------")
        cur.close()
        db.commit()
        db.close()
        return "数据已解析，并保存在MySQL数据库contest下的PopularAttractions表中，请前往查看！"

if __name__ == "__main__":
    print("===========去哪儿网===========")
    slc = spiders_province_people_area()
    return_base_url = slc.imitate_click()
    return_page_list = slc.input_page()
    return_htmls = slc.load_page(return_base_url, return_page_list)
    startTime = time.time()
    print("--------开始时间(解析页面):", startTime, "---------")
    return_items = slc.parse_page(return_htmls)
    return_item_row = ["用户", "出发日期", "历经时长", "城市", "景点", "拍摄数量", "标签"]
    # print(return_items)
    return_new_items = slc.data_pretreatment(return_items, return_item_row)
    slc.save_file(return_new_items)
    print("--------CSV数据解析完成，花费:", time.time() - startTime, "---------")
    # print(return_new_items)
    slc.save_mysql(return_new_items)
    print("--------MySQL数据解析完成，花费:", time.time() - startTime, "---------")

    # print("===========马蜂窝网===========")
    # shc = spider_hot_city()
    # data = shc.hot_city_tourist()
    # head = ['城市', '去过的人']
    # shc.save_csv(head, data)
    # shc.save_mysql(data)

    # print("===========携程网===========")
    # scw = spider_city_want()
    # scw.parse_data()
    # data = scw.getdata(scw.popular_city, scw.city_name, scw.headers)
    # scw.save_mysql(data)

    # print("===========飞猪网===========")
    # scm = spider_city_money()
    # data = scm.parse_page()
    # head = ["景点", "城市", "当月销量", "优惠价", "价格"]
    # scm.save_csv(head, data)
    # scm.save_mysql(data)