from sqlalchemy import insert
from tables import user_table
from connect import engine

# statment = insert(user_table).values(name = "Marijona",fullname="qazxsw")
statement = insert(user_table)

with engine.connect() as conn:
    conn.execute(statement,[
            {'name': "Tes1",'fullname':"comp1"},
            {'name': "Test2",'fullname':"comp2"}          
                 ])
    conn.commit()


# print(statment)

