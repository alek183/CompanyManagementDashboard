from fastapi import FastAPI
from routes import router
from database import create_database

app = FastAPI()
app.include_router(router)

create_database()

@app.get("/")
def root():
    return {"message": "Up and runnin!"}
