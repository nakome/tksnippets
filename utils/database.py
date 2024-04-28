from sqlite3 import *
import os


class database:

    def __init__(self):
        self.conn = connect("./storage/data.db")

    def get_all(self):
        sql = "SELECT uid,title,description,content,created,category FROM snippets"
        try:
            results = self.conn.execute(sql)
            return results.fetchall()
        except OperationalError as e:
            raise e

    def get_by_uid(self, uid):
        sql = 'SELECT uid, title, description, content, created, category FROM snippets WHERE uid = ?'
        try:
            # Utiliza consulta parametrizada para evitar inyección de SQL
            results = self.conn.execute(sql, (uid,))
            return results.fetchone()
        except OperationalError as e:
            raise e


    def find_by_title(self, txt):
        sql = 'SELECT uid, title, description, content, updated, category FROM snippets WHERE title LIKE ? OR category LIKE ?'
        try:
            results = self.conn.execute(sql, ('%' + txt + '%', '%' + txt + '%'))
            return results.fetchall()
        except OperationalError:
            raise


    def set(self, *args):

        sql = """ INSERT INTO snippets
                  VALUES (null, ?, ?, ?, CURRENT_TIMESTAMP, ?)"""
        try:
            self.conn.execute(sql, (args[0], args[1], args[2], args[3]))
        except OperationalError as e:
            raise e
        else:
            self.conn.commit()

    def update(self, *args):

        sql = """ UPDATE snippets
                  SET title = ? ,
                      description = ? ,
                      content = ?,
                      category = ?,
                      updated = CURRENT_TIMESTAMP
                  WHERE uid = ?"""
        try:
            self.conn.execute(sql, (args[1], args[2], args[3], args[4], args[0]))
        except OperationalError as e:
            raise e
        else:
            self.conn.commit()

    def delete_uid(self, uid):
        sql = 'SELECT uid, title, description, content, created, category FROM snippets WHERE uid = ?'
        try:
            results = self.conn.execute(sql, (uid,))
            return results.fetchone()
        except OperationalError as e:
            raise e
