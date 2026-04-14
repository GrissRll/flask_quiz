from flask import Flask, render_template
from data_base.db import DataBase
from data_base.querys import SL_ALL_QUIZ
import os

DATABASE = "/flask_quiz/quiz_data.db"
DEBUG = True
SECRET_KEY = "some_secret_key"

app = Flask(__name__)
app.config.from_object(__name__)
app.config.update(dict(DATABASE=os.path.join(app.root_path, "quiz_data.db")))

db = DataBase(app.config.get("DATABASE"))


@app.get("/")
def index():
    print(db.get_data(SL_ALL_QUIZ))
    return "hello world Griss!"


if __name__ == '__main__':
    app.run(debug=True)
