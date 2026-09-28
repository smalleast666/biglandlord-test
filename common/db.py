
import pymysql


def get_connection():

    return pymysql.connect(
        host="localhost",
        port=3306,
        user="root",
        password="root",
        database="big_landlord",
        charset="utf8mb4"
    )


def query_one(sql, params=None):

    connection = get_connection()

    try:
        cursor = connection.cursor(pymysql.cursors.DictCursor)

        cursor.execute(sql, params)

        return cursor.fetchone()

    finally:
        cursor.close()
        connection.close()

