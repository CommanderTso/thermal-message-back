from flask_login import UserMixin
import sqlite3, os
from flask_bcrypt import generate_password_hash, check_password_hash

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
        c.close()
        
        if result == None:
            # None is expected by flask-login where no record exists
            return None
        else:
            instance = super().__new__(cls)
            instance.password = result[3]
            instance.first_name = result[2]
            instance.email = result[1]
            instance.id = result[0]
            return instance

    def set_password(self, password):
        conn = sqlite3.connect(os.environ['TPB_DB'])
        c = conn.cursor()

        new_hash = generate_password_hash(password).decode('UTF-8')
        print(f'new hash: {new_hash}')
        print(f'id: {self.id}')
        query = "UPDATE users SET password = $1 WHERE id = $2"
        params = (new_hash, self.id)
        
        # TODO - sanity check on what we're settting password to
        c.execute(query, params)
        conn.commit()
        c.close()


    def check_password(self, password):
        conn = sqlite3.connect(os.environ['TPB_DB'])
        c = conn.cursor()

        query = "SELECT password from users WHERE id = $1"
        params = (self.id,)
        c.execute(query, params)
        result = c.fetchone()
        pw_hash = result[0]

        print(f'password from db: "{result[0]}" from user id {self.id}')
        print(f'check_password_hash: {check_password_hash(pw_hash, password)}')
        
        return check_password_hash(pw_hash, password)

