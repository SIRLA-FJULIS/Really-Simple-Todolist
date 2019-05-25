import os
from app import create_app, db
from app.models import TaskDate, TaskItem
from flask_migrate import Migrate

#建立一個App，從環境變數或預設來取得組態設置。
app = create_app(os.getenv('FLASK_CONFIG') or 'default')

##初始化Flask-Migrate
migrate = Migrate(app, db)

##Python殼層的自訂context
@app.shell_context_processor
def make_shell_context():
    return dict(db=db, TaskDate=TaskDate, TaskItem=TaskItem)
    
### 單元測試 ###
@app.cli.command()
def test1():
    """Run the unit tests."""
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)