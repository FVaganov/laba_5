from fastapi import FastAPI
from dotenv import load_dotenv
import os

import uvicorn

load_dotenv()  # Загружаем переменные из .env

app = FastAPI()

@app.get("/")
def read_root():
    return {
        "message": "Hello from FastAPI",
        "database_url": os.getenv("DATABASE_URL"),
        "debug_mode": os.getenv("DEBUG")
    }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)  # Важно!