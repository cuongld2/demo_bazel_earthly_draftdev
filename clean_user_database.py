from user_app import crud
from user_app.database import SessionLocal

db = SessionLocal()
crud.remove_all_users(db)
db.close()
