from flask_login import UserMixin
import sqlite3, os

class User(UserMixin):
    def __new__(cls, email=None, id=None):
        conn = sqlite3.connect(os.environ['TPB_DB'])
        c = conn.cursor()
        
        result = None
        if email is not None:
            query = "SELECT * FROM users WHERE email = ?"
            param = email
        elif id is not None:
            query = "SELECT * FROM users WHERE id = ?"
            param = id
        else:
            # TODO - handle this more robustly
            raise "User constructor not passed either id or email"

        c.execute(query, (param,))
        
        result = c.fetchone()
        print(f"User from db: {result}")
        c.close()
        
        if result == None:
            # None is expected by flask-login where no record exists
            return None
        else:
            instance = super().__new__(cls)
            instance.first_name = result[2]
            instance.email = result[1]
            instance.id = result[0]
            return instance

    def set_password(self, id, password):
        # take password, hash it, commit to DB
        pass

    def check_password(self, username, password):
        return True
        # take input'd password, hash, check against hash in db
