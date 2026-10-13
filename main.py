from fastapi import FastAPI

app = FastAPI()    # here app is variable & FastAPI is Object

@app.get("/")       # path
def home():        # define a Function
    return {"message":"Hello without venv"}
