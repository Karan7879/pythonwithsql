import psycopg2
from psycopg2 import extras

hostname = "localhost"
database = "lear_pg"
username = "postgres"
pwd = "12345"
port_id = 5432
cur =None
conn = None
try:
    conn = psycopg2.connect(
        host = hostname,
        dbname = database,
        user = username,
        password = pwd,
        port = port_id
    )
    cur = conn.cursor(cursor_factory=extras.DictCursor)
    # cur.execute('DROP TABLE IF EXISTS')
    create_script = ''' CREATE TABLE IF NOT exists employee(
                        id  int PRIMARY KEY,
                        name varchar(40) Not Null,
                        salary int,
                        dept_id varchar(30)                    
    )
'''
    cur.execute(create_script)
    # insert_script  = 'INSERT INTO employee(id,name,salary,dept_id) values(%s,%s,%s,%s)'
    # inser_value = [(2,'Rohan',200000,'SWE1'),(3,'John',300000,'SWE2'),(4,'Qohan',40000,'Product Manager')]
    # cur.executemany(insert_script,inser_value)
    cur.execute('SELECT * from employee')
    # print(cur.fetchall()) 
    for record in cur.fetchall():
        print(record['name'],record['salary'])
    
    update_script = 'UPDATE employee SET salary = salary + (salary*1.5)'
    cur.execute(update_script)

    cur.execute('SELECT * from employee')
    for record in cur.fetchall():
        print(record['name'],record['salary'])

    delete_script = 'DELETE FROM employee WHERE name = %s'
    delete_record = ('Rohan',)
    cur.execute(delete_script,delete_record)
    cur.execute('SELECT * from employee')
    for record in cur.fetchall():
        print(record['name'],record['salary'])

    conn.commit()
except Exception as error:
    print(error)
finally:
    if cur is not None:
        cur.close()
    if conn is not None:
        conn.close()

