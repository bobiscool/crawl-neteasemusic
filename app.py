#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask
import config


# 应用工厂：将app的设置在函数中设置 (http://flask.pocoo.org/docs/0.11/patterns/appfactories/)
def create_app():
    app = Flask(__name__, template_folder='templates',
                static_floder='static')
    # 配置
    app.config.from_object(config)
    # 初始化扩展
    mako.init_app(app)
    db.init_app(app)

    return app


# 应用
app = create_app()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8100, debug=app.debug)
