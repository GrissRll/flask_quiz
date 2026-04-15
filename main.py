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


@app.route("/", methods=["GET", "POST"])
def index():
    quiz = db.get_data(SL_ALL_QUIZ)
    if not session.get("q_num"):
        session["q_num"] = 1
        session["user_answers"] = []
    if request.method == "POST":
        session["q_num"] = 1
        session["quiz_id"] = request.form.get("quiz_list")
        session["question_list"] = db.get_data(SL_QUESTION, session["quiz_id"])
        return redirect(url_for("test"))
    return render_template("index.html", quiz_list=quiz, title="ТОП ВИКТОРИНЫ!")


@app.route("/test", methods=["GET", "POST"])
def test():
    if session["q_num"] == len(session["question_list"]):
        return redirect(url_for("result"))

    full_q = session["question_list"][session["q_num"]]
    q_list = full_q[1:]
    question = full_q[0]
    if request.method == "POST":
        session["q_num"] += 1
        user_ans = request.form.get("answer")
        session["user_answers"].append(user_ans)
        return redirect(url_for("test"))

    return render_template("test.html", q_list=q_list, question=question)


@app.route("/result")
def result():
    return "results"


if __name__ == '__main__':
    app.run(debug=True)
