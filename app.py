from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "It updates in real time!"}
