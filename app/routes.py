from flask import render_template
from app import app

@app.route('/')
def index():
    return render_template('index.html')

# 其他路由和视图函数稍后再定义
