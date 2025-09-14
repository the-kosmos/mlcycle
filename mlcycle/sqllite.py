from mlcycle.save import SaveMethod
import sqlite3

class SqlLite(SaveMethod):
    def __init__(self, db=sqlite3.connect("mlcycle.db")):
        self.db = db
        self.db.execute("CREATE TABLE metrics (id STRING PRIMARY KEY, value REAL)")

    def log_metric(self, val):
        pass
        # self.db.cursor().execute("insert into metric values (?, ?)", val)
