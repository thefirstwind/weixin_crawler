# import eventlet
# eventlet.monkey_patch()
from flask import Flask
from flask_cors import CORS,cross_origin
from flask_socketio import SocketIO
import redis
from configs.auth import REDIS_HOST,REDIS_PORT,REDIS_DB


class CustomFlask(Flask):
    jinja_options = Flask.jinja_options.copy()
    jinja_options.update(dict(
        variable_start_string='[[',  # Default is '{{', I'm changing this because Vue.js uses '{{' / '}}'
        variable_end_string=']]',
    ))


# 定义作为web服务器常用的公用实例对象 方便其余程序直接import
app = CustomFlask('WeixinCrawler',template_folder="./ui/templates",static_folder="./ui/static")
# app = CustomFlask('WeixinCrawler',template_folder="./templates",static_folder="./static")
app.config['SECRET_KEY'] = 'secret!'
app.config['origin'] = "http://localhost:5000"
app.config['Access-Control-Allow-Origin'] = "http://localhost:5000"
app.config['Access-Control-Allow-Credentials'] = True
app.config['Access-Control-Allow-Headers'] ='Origin,X-Requested-With,Content-Type,Accept,content-type,application/json,Authorization'
app.config['Access-Control-Allow-Methods'] = 'GET,PUT,POST,DELETE,OPTIONS'
# app.config['CORS_AUTOMATIC_OPTIONS'] = True
# app.config['CORS_SUPPORTS_CREDENTIALS'] = True


# socketio = SocketIO(app)
# socketio = SocketIO(app, async_mode='gevent')
socketio = SocketIO(app, async_mode='gevent',cors_allowed_origins="*")

the_redis = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT, db=REDIS_DB)
