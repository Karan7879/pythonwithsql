from sqlalchemy import delete
from tables import user_table
from connect import engine

statement = delete(user_table).where(
    user_table.c.id==3
)

print(statement)

with engine.connect() as conn:
    conn.execute(statement)
    conn.commit()




