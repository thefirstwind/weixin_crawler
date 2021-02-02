# import eventlet
# eventlet.monkey_patch()
from flask import Flask
from flask_cors import CORS
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
app.config['CORS_HEADERS'] = 'Content-Type'
cors = CORS(app, resources={r"/socket.io": {"origins": "http://118.190.146.172:5000"}})

CORS(app)
@app.route("/")
@cross_origin(origin='118.190.146.172',headers=['Content- Type','Authorization'])

# socketio = SocketIO(app)
socketio = SocketIO(app, async_mode='gevent', cors_allowed_origins="*")
the_redis = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT, db=REDIS_DB)
