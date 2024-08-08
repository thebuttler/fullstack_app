from flask import Flask
from config import Config
from models import db, About
from views import main_blueprint

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

with app.app_context():
    db.create_all()

app.register_blueprint(main_blueprint)


@app.route('/')
def hello_world():
    return "Flask API is running!"


if __name__ == '__main__':
    app.run(debug=True, port=8080)