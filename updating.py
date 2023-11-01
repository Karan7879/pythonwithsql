from tables import user_table
from connect import engine
from sqlalchemy import update

statement = update(user_table).where(
    user_table.c.name == "Test6"
).values(name="Testing")

with engine.connect() as conn:
    conn.execute(statement)
    conn.commit()

# print(statement)



