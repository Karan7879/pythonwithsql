from tables import user_table
from sqlalchemy import select
from connect import engine

statement = select(user_table).where(user_table.c.name =="Test1")

with engine.connect() as conn:
    result = conn.execute(statement)

    for i in result:
        print(f"id: = {i.id},user:{i.name}")





