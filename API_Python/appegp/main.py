import sys
import os
from fastapi import FastAPI, File, UploadFile
from appegp.src.analyzer import analyze_egp_file

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Welcome to the API_Python application!"}


@app.post("/upload-egp/")
async def upload_egp(file: UploadFile = File(...)):
    file_location = f"files_egp/{file.filename}"
    os.makedirs(os.path.dirname(file_location), exist_ok=True)
    with open(file_location, "wb+") as file_object:
        file_object.write(file.file.read())

    tables = analyze_egp_file(file_location)
    return {"tables": tables}
