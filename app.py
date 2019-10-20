#-*- coding:utf-8 -*-
# author:Agam
# datetime:2018-11-05
import os
from dotenv import load_dotenv

#不使用Flask内置服务器时，需要手动加载环境变量
dotenv_path = os.path.join(os.path.dirname(__file__), '.env')

if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

from flask_admin import app

if __name__ == '__main__':
    # app.run(host='127.0.0.1', debug=True, port=5002)
    app.run()