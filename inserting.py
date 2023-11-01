from sqlalchemy import insert
from tables import user_table
from connect import engine

# statment = insert(user_table).values(name = "Marijona",fullname="qazxsw")
statement = insert(user_table)

with engine.connect() as conn:
    conn.execute(statement,[
            {'name': "Tes3",'fullname':"comp3"},
            {'name': "Test4",'fullname':"comp4"},
            {'name': "Tes5",'fullname':"comp5"},
            {'name': "Test6",'fullname':"comp6"}            
                 ])
    conn.commit()


# print(statment)

