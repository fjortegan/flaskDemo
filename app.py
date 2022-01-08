from flask import Flask
from users import blueprint as api_user
from model import init_db

app = Flask(__name__)
init_db(app)
app.register_blueprint(api_user, url_prefix="/api/")

if __name__ == '__main__':
    app.run(debug=True)
