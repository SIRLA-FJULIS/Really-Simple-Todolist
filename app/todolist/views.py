from flask import render_template
import datetime
from . import todolist   #C:\Users\pcsh1\Pictures\flask_proj\app\todolist
from .forms import ToDoListForm #表單物件   #C:\Users\pcsh1\Pictures\flask_proj\app\todolist\
from .. import db        #C:\Users\pcsh1\Pictures\flask_proj\
from ..models import TaskDate, TaskItem    #C:\Users\pcsh1\Pictures\flask_proj\app

#路由裝飾器來自藍圖(todolist.route)
@todolist.route('/', methods=['GET', 'POST'])
def index():
    date = None
    item = None
    form = ToDoListForm()
    if form.validate_on_submit():
        # 用表單收到的item在資料庫中查詢
        item = TaskItem.query.filter_by(item=form.item.data).first()
        if item is None:
            # 查無此item的話，將該date, item寫入資料庫
            date = TaskDate(date=form.date.data)
            db.session.add(date)
            item = TaskItem(item=form.item.data)
            db.session.add(item)
            db.session.commit()
        form.date.data = ''
        form.item.data = ''
    return render_template('index.html', form=form, date=date, item=item)