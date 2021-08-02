import mysql.connector
from mysql.connector import cursor

anime_db = mysql.connector.connect(
    host = "remotemysql.com",
    user = "1BT0P36KhA",
    password = "Wwng1zQpuK",
    database = "1BT0P36KhA",
    port = "3306"
)

db_cursor = anime_db.cursor()

# Insert anime data in anime_database table with columns having anime name and episodes in from of JSON
def insert_anime(name, episodes):
    sql = "INSERT INTO anime_database (name, episodes) VALUES (%s, %s)"
    val = (name, episodes)
    db_cursor.execute(sql, val)
    anime_db.commit()

# Clears all the data inside anime_database table
def truncate_table():
    sql = "TRUNCATE anime_database"
    db_cursor.execute(sql)

truncate_table()