#!/usr/bin/env python3
import os
from app import create_app
from flask_script import Manager, Server
from spider import main_spider
from flask_script import Manager
from app import db1
from flask import Flask
from flask_migrate import Migrate

app = Flask(__name__)


app = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app)

server = Server(host="127.0.0.1", port=5001)
manager.add_command("runserver", server)
migrate = Migrate(app=app, db1=db1)





if __name__ == '__main__':
    manager.run()
