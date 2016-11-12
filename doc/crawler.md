# 爬虫

## 安装

使用`lxml`作为解析网页的工具，这个库需要依赖`libxml2`, `libxslt`。先安装它们（以mac为例）:

    brew install libxml2
    brew install libxslt
    brew link libxml2 --force
    brew link libxslt --force

安装 `lxml`:

    source venv/bin/activate
    pip install lxml 

安装 `requests`

    pip install requests

安装 `fake-useragent`:

    pip install fake-useragent

安装 `pycrypto` 和 `futures`

    pip install pycrypto futures

安装 `flask` , `mongoengine` 和 `redis`

    pip install flask
    pip install flask-mako flask-mongoengine redis

## 构建flask应用目录

* 本地配置：local_settings.py
* 配置文件：config.py
* flask扩展：ext.py
* app.py




