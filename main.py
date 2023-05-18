from typing import Union
from fastapi import FastAPI
from mangum import Mangum

app = FastAPI()

@app.get("/")
def root():
    return {
        "message": "Hello World"
    }

@app.get("/items/{item_id}")
def get_item(item_id: int, q: Union[str, None] = None):
    return {
        "item_id": item_id,
        "data": q
    }

handler = Mangum(app, lifespan="off")