import uvicorn
from db import db_connection
from fastapi import FastAPI
from routes.rout import router as rout


app = FastAPI()
app.include_router(rout)

if __name__ == "__main__":
    uvicorn.run("main:app", port=8009)