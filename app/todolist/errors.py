from flask import render_template
from . import todolist

# 全域(app_errorhandler裝飾器)的錯誤處理函式 #

@todolist.app_errorhandler(404)     #路由裝飾器來自藍圖(main.route)
def page_not_found(e):
    return render_template('404.html'), 404
    
@todolist.app_errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500