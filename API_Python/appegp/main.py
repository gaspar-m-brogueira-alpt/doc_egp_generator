from fastapi import FastAPI
from appegp.api.v1.endpoints import example

app = FastAPI()

app.include_router(example.router, prefix="/api/v1/example", tags=["example"])


@app.get("/")
def read_root():
    return {"message": "Welcome to the API_Python application!"}
