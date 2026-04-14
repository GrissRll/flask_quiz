from flask import Flask, render_template, request, session, redirect, url_for
from data_base.db import DataBase
from data_base.querys import SL_ALL_QUIZ, SL_QUESTION
import os

DATABASE = "/flask_quiz/quiz_data.db"
DEBUG = True
SECRET_KEY = "some_secret_key"

app = Flask(__name__)
app.config.from_object(__name__)
app.config.update(dict(DATABASE=os.path.join(app.root_path, "quiz_data.db")))

db = DataBase(app.config.get("DATABASE"))


@app.route("/", methods=["GET","POST"])
def index():
    quiz = db.get_data(SL_ALL_QUIZ)
    if request.method == "POST":
        session["quiz_id"] = request.form.get("quiz_list")
        session["question_list"] = db.get_data(SL_QUESTION, session["quiz_id"])
        return redirect(url_for("test"))
    return render_template("index.html", quiz_list=quiz, title="ТОП ВИКТОРИНЫ!")

@app.route("/test", methods=["GET", "POST"])
def test():
    print(session["question_list"])
    return "test page"

if __name__ == '__main__':
    app.run(debug=True)
