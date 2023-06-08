## 锦绣中华旅游数据可视化交互平台  简介
锦绣中华旅游数据可视化交互平台是一个Python环境下的WEB后台管理系统脚手架，目标是用极少量的代码，快速构建小型WEB应用。

1. 使用较传统的重后端+轻前端的方式，降低总体代码量
2. Web框架使用Flask，默认Jinja模版
3. ORM框架使用Peewee
4. 前端套用基于BootStrap的AdminLTE模板

## 第三方依赖
- peewee
- pymysql
- flask
- flask-script
- flask-wtf
- flask-login


## 环境配置
### 第三方依赖安装
```
pip3 install -r requirements.txt

```
### 系统参数配置
1. 编辑`config.py`， 修改SECRET_KEY及MySQL数据库相关参数
```
SECRET_KEY = os.environ.get('SECRET_KEY') or 'your-secret'
DB_HOST = '127.0.0.1'
DB_USER = 'root'
DB_PASSWD = 'root'
DB_DATABASE = 'contest'
```

### 数据库初始化
1. 自动建表
直接运行`models.py`

2. 插入管理员用户（默认admin/admin)
```
INSERT INTO `user` (`id`, `username`, `password`, `fullname`, `email`, `phone`, `status`)
VALUES
	(1, 'admin', 'pbkdf2:sha1:1000$Km1vdx3W$9aa07d3b79ab88aae53e45d26d0d4d4e097a6cd3', '管理员', 'admin@admin.com', '18612341234', 1);
```

### 启动应用
```
manage.py 
```


## 项目目录结构
- /app/auth  用户认证相关代码
- /app/main  主要功能点相关代码
- /app/static  JS、CSS等静态文件
- /app/template  页面模版
- /app/models.py  Peewee模型
- /app/utils.py  工具模块
- /conf  系统参数及日志配置


## 相关学习文档
- [http://flask.pocoo.org](http://flask.pocoo.org)
- [https://flask-login.readthedocs.io](https://flask-login.readthedocs.io)
- [https://flask-script.readthedocs.io](https://flask-script.readthedocs.io)
- [https://flask-wtf.readthedocs.io](https://flask-wtf.readthedocs.io)
- [http://docs.peewee-orm.com](http://docs.peewee-orm.com)
- [https://almsaeedstudio.com/preview](https://almsaeedstudio.com/preview)

