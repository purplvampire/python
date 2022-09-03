#! python3
import sqlite3

# 建立SQLite DB連線
connection = sqlite3.connect("data.db")

# 轉換型別為字典(預設是Tuple)
connection.row_factory = sqlite3.Row


def create_table():
    # 執行Session
    with connection:
        # 建立新表單
        connection.execute("CREATE TABLE IF NOT EXISTS entries (content TEXT, date TEXT);")


def add_entry(entry_content, entry_date):
    # 建立一筆資料到entries資料表
    with connection:
        connection.execute(
            "INSERT INTO entries VALUES (?, ?);", (entry_content, entry_date)
        )
    

# 表列清單中的資料
def get_entries():
    # 取出的值因型別轉換變成字典
    cursor = connection.cursor().execute("SELECT * FROM entries;")
    return cursor

    