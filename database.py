import sqlite3

conn = sqlite3.connect("schulich_database.db")
cursor = conn.cursor()

sql = """CREATE TABLE IF NOT EXISTS schulich_leaders (
         leader_url varchar(255) PRIMARY KEY,
         leader_name varchar(255) NOT NULL,
         program_name varchar(30) NOT NULL,
         university_name varchar(50) NOT NULL,
         year varchar(10) NOT NULL
         );"""

cursor.execute(sql)
conn.commit()
conn.close()


def add_row(information):
    local_conn = sqlite3.connect("schulich_database.db")
    local_cursor = local_conn.cursor()

    row = f'''INSERT INTO schulich_leaders (leader_url, leader_name, program_name, university_name, year)
    VALUES(?, ?, ?, ?, ?)'''
    local_cursor.execute(row, information)
    local_conn.commit()
    local_conn.close()
