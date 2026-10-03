from fastapi import FastAPI
from datetime import datetime

app = FastAPI()


@app.get("/status")
def status():
    return {
        "message": "Server is healthy",
        "timestamp": datetime.now()
    }