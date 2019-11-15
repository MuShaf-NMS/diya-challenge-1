from database.mysql_connect import DatabaseMysql
from datetime import date

db = DatabaseMysql()
a = db.get_siswa()
for i in a:
    print(i)