import datetime
import psycopg2
conn = psycopg2.connect(
    database = "postgres",
    user = "postgres",
    port = 5432,
    password = "trisha123",
    host = "localhost"
)
def create_table():
    with conn.cursor() as cursor:
        cursor.execute("create table if not exists  student(id serial primary key,name text not null);")
        cursor.execute("create table if not exists attendance(id serial primary key,student_id int references student(id),date DATE not null, status boolean default TRUE);")
    conn.commit()
def add_student(name):
    with conn.cursor() as cursor:
        cursor.execute("insert into student(name) values(%s);",(name,))
    conn.commit()
def mark_attendance(student_id,status = True):
    with conn.cursor() as cursor:
        cursor.execute("insert into attendance(student_id,date,status) values(%s,%s,%s);",(student_id,datetime.datetime.today(),status))
    conn.commit()
def view_attendance(student_id):
    with conn.cursor() as cursor:
        cursor.execute("""select s.name,a.date,a.status
                     from student as s 
                     join attendance as a 
                     on s.id = a.student_id
                     where s.id = %s""",(student_id,))
        rows = cursor.fetchall()
        for row in rows:
            status = "✅ Present" if row[2] else "❌ Absent"
            print(f"name : {row[0]}  | date : {row[1]}   | status : {status}")
def summary():
    with conn.cursor() as cursor:
        cursor.execute("""select s.name,count(*) FILTER (where a.status = TRUE) as present,count(*)
                      FILTER (where a.status = FALSE) as absent
                      from student as s 
                      left join attendance as a
                      on s.id = a.student_id 
                     group by s.id
                     """)
        result = cursor.fetchall()
        for row in result:
            print(f"{row[0]} -> present_count : {row[1]} -> absent_count : {row[2]}")


