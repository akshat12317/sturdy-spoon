import sqlite3 as sql
def connect():
    return sql.connect('db.sqlite3')
def process(query):
    try:
        db=connect()
        db.execute(query)
        db.commit()
        return 'table created'
    except Exception as e:
        print(e)


def create_table():
    query="CREATE TABLE info(id integer primary key autoincrement,name text,mobile integer unique,email text)"
    process(query)


def insert_data(name,mobile_no,email):
    query=f"insert into info values(null,'{name}',{mobile_no},'{email}')"
    process(query)
    return 'data added to the data base'


def Show():
    query="select * from info"
    try:
        db=connect()
        result = db.execute(query)
        data = result.fetchall()  # fetches the data
        return data
    except Exception as e:
        print(e)



