import uvicorn
from db import db_connection
from fastapi import FastAPI
from routes.rout import router as rout


app = FastAPI()
app.include_router(rout)

def main():
    db_connection.create_table()

if __name__ == "__main__":
    main()
    uvicorn.run("main:app", port=8009)