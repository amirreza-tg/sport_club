from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Hello FastAPI"}


@app.get("/ali")
def home():
    return {"message": "Hello Ali"}