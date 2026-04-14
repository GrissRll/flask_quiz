CT_QUIZ = """
    CREATE TABLE IF NOT EXISTS quiz(
        id INTEGER PRIMARY KEY,
        name VARCHAR
    )
"""

CT_QUESTION = """
    CREATE TABLE IF NOT EXISTS question(
        id INTEGER PRIMARY KEY,
        question VARCHAR,
        answer VARCHAR,
        wrong1 VARCHAR,
        wrong2 VARCHAR,
        wrong3 VARCHAR
    )
"""

CT_QUIZ_CONT = """
    CREATE TABLE IF NOT EXISTS quiz_content(
        id INTEGER PRIMARY KEY,
        quiz_id INTEGER,
        question_id INTEGER,
        
        FOREIGN KEY (quiz_id) REFERENCES quiz (id),
        FOREIGN KEY (question_id) REFERENCES question (id)
    )
"""

DROP_TBS = """
    DROP TABLE IF EXISTS quiz;
    DROP TABLE IF EXISTS question;
    DROP TABLE IF EXISTS quiz_content;
"""

SL_ALL_QUIZ = """
    SELECT * FROM quiz
"""

INS_QUIZ = """
    INSERT INTO quiz(name) VALUES(?)
"""

INS_QUEST = """
    INSERT INTO question(question, answer, wrong1, wrong2, wrong3) VALUES(?,?,?,?,?)
"""

INST_QC = """
    INSERT INTO quiz_content(quiz_id, question_id) VALUES(?,?)
"""
