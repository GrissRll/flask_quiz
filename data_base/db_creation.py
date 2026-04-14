from .querys import *
from .start_datas_quiz import *

def create_db(db):
    #CLEAR DATABASE
    db.exc_script(DROP_TBS)

    #CREATE TABLES IN DATABASE
    db.insert_data(CT_QUIZ)
    db.insert_data(CT_QUESTION)
    db.insert_data(CT_QUIZ_CONT)

    #ADD DATA INTO TABLES
    db.insert_data(INS_QUIZ, quiz_names, False)
    db.insert_data(INS_QUEST, memes_question, False)
    db.insert_data(INST_QC, link_list, False)


