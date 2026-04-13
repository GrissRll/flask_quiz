from querys import *
from db import DataBase

db = DataBase()

#CLEAR DATABASE
db.exc_script(DROP_TBS)

#CREATE TABLES IN DATABASE
db.insert_data(CT_QUIZ)
db.insert_data(CT_QUESTION)
db.insert_data(CT_QUIZ_CONT)

