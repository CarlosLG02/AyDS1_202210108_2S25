from fastapi import FastAPI

app = FastAPI()

@app.get("/album")
def read_item():
    return {"Album": "Unlimited Love"}
