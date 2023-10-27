from app import app, db
from app import UsersTable
from flask_bcrypt import Bcrypt

app.app_context().push()

def create_new_user(username, password):
    bcrypt = Bcrypt(app)
    password_hash = bcrypt.generate_password_hash(password).decode('utf-8')
    user = UsersTable(username=username, password_hash=password_hash)
    db.session.add(user)
    db.session.commit()

if __name__ == "__main__":

    username = "username"
    password = "password"

    create_new_user(username, password)

    print("New user inserted successfully.")
