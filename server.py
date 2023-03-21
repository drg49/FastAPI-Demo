from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def index():
    return "The server is up and running."

@app.get("/param/{val}")
async def param(val):
    return val
