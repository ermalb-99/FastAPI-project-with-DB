from fastapi import FastAPI,Depends,Body,Path
from sqlalchemy.orm import Session
import models
from database import SessionLocal



app = FastAPI()

def get_db():
     db = SessionLocal()
     try:
          yield db
     finally:
          db.close()

@app.get('/database')
async def return_all_data(db:Session=Depends(get_db)):
     return db.query(models.Todos).all()

@app.get('/database/{todo_id}')
async def read_todo_by_id(todo_id: int = Path(..., title="Todo ID", description="The ID of the todo item to retrieve"), db: Session = Depends(get_db)):
    todo = db.query(models.Todos).filter(models.Todos.id == todo_id).first()
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    return todo






















# from fastapi import FastAPI, Depends
# from sqlalchemy.orm import Session
# import models
# from database import engine, SessionLocal

# app = FastAPI()
# # INSTANCA E FASTAPI

# models.Base.metadata.create_all(bind=engine)
# # Krijuesi i datbazes 

# # FUNKSIONI I CILI HAP DATABAZEN DHE MBYLL 
# def get_db():
#      db = SessionLocal()
#      try:
#           yield db
#      finally:
#           db.close()


# # Funksioni Get i fastapi
# @app.get('/')
# async def return_all_data(db: Session = Depends(get_db)):
#      return db.query(models.Todos).all()