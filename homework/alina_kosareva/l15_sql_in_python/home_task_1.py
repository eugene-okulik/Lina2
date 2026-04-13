import mysql.connector as mysql

db = mysql.connect(
    username="st-onl",
    password="AVNS_tegPDkI5BlB2lW5eASC",
    host="db-mysql-fra1-09136-do-user-7651996-0.b.db.ondigitalocean.com",
    port=25060,
    database="st-onl",
)
cursor = db.cursor(dictionary=True)
# Создание студента

query = "INSERT INTO students(name,second_name) VALUES (%s,%s)"
values = ("Robby", "Piterson")
cursor.execute(query, values)
user_id = cursor.lastrowid
cursor.execute("SELECT * FROM students WHERE id = %s", (user_id,))
print(cursor.fetchone())
print(user_id)

# Создание группы

query = "INSERT INTO `groups` (title,start_date,end_date) VALUES(%s,%s,%s)"
values = ("Python Core Step2", "April 6", "May 26")
cursor.execute(query, values)
group_id = cursor.lastrowid
cursor.execute("SELECT * FROM `groups` WHERE id = %s", (group_id,))
print(cursor.fetchone())
print(group_id)

# Определение студента в группу
query = """
UPDATE students
SET group_id = %s
WHERE id=%s
"""

cursor.execute(query, (group_id, user_id))
cursor.execute("SELECT * FROM students WHERE id = %s", (user_id,))
print(cursor.fetchone())

# Создание несколько книг (books) и указание, что созданный студент взял их
query = "INSERT INTO books(title,taken_by_student_id) VALUES (%s,%s);"
values = [
    (
        "Изучаем Python",
        user_id,
    ),
    (
        "Python for QA",
        user_id,
    ),
]
cursor.executemany(query, values)

# Создание нескольких учебных предметов (subjects)
query = "INSERT INTO subjects (title) VALUES (%s);"
values = [("Python Core",), ("Python for QA",)]
subject_id = []
for subject in values:
    cursor.execute(query, subject)
    subject_id.append(cursor.lastrowid)
print(subject_id)

# Создайте по два занятия для каждого предмета (lessons)
query = "INSERT INTO lessons (title,subject_id) VALUES(%s,%s)"
values = [
    (
        "Classes in Python",
        subject_id[0],
    ),
    (
        "OOP in python",
        subject_id[0],
    ),
    (
        "Page object model ",
        subject_id[1],
    ),
    (
        "Playwright core",
        subject_id[1],
    ),
]
lesson_id = []
for lesson in values:
    cursor.execute(query, lesson)
    lesson_id.append(cursor.lastrowid)
print(lesson_id)

# Поставьте своему студенту оценки (marks) для всех созданных вами занятий
query = "INSERT INTO marks (value,lesson_id,student_id) VALUES(%s,%s,%s)"
values = [
    (
        7,
        lesson_id[0],
        user_id,
    ),
    (
        8,
        lesson_id[1],
        user_id,
    ),
    (
        9,
        lesson_id[2],
        user_id,
    ),
    (
        9,
        lesson_id[3],
        user_id,
    ),
]
cursor.executemany(query,values)
cursor.execute("SELECT * FROM marks m WHERE student_id = %s", (user_id,))
print(cursor.fetchall())

# Вывод всех данных о студенте
query = """ SELECT * FROM `groups` g
JOIN students s on g.id = s.group_id
JOIN books b on b.taken_by_student_id = s.id
JOIN marks m on s.id =m.student_id
JOIN lessons l on m.lesson_id =l.id
JOIN subjects s2 on s2.id  = l.subject_id
WHERE s.id=%s"""

cursor.execute(query, (user_id,))
print(cursor.fetchall())

db.commit()
db.close()
