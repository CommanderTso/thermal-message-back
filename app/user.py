from flask_login import UserMixin
import sqlite3, os

class User(UserMixin):
    def __new__(cls, id):
        conn = sqlite3.connect(os.environ['TPB_DB'])
        c = conn.cursor()
        
        c.execute("""
            SELECT *
            FROM users
            WHERE id = ?
        """,
        (id,))

        result = c.fetchone()
        c.close()
        
        if result == None:
            # None is expected by flask-login where no record exists
            return None
        else:
            instance = super().__new__(cls)
            instance.name = result[1]
            instance.id = result[0]
            return instance

    def setPassword(self, id, password):
        # take password, hash it, commit to DB
        pass

    def checkPassword(self, id, password):
        pass
        # take input'd password, hash, check against hash in db
