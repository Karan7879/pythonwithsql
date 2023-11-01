from connect import engine
from tables import user_table,comments_table,meta_obj


print(">>>create DB")
meta_obj.create_all(bind=engine)



