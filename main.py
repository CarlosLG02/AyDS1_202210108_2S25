from fastapi import FastAPI

app = FastAPI()

@app.get("/song")
def read_item():
    return {"Song": "Scar Tissue"}
