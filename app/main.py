from typing import Union, Dict

from fastapi import FastAPI
from pydantic import BaseModel
from starlette.responses import JSONResponse

app = FastAPI()
global dicted_item


class Item(BaseModel):
    user_id: str
    password: str


@app.get("/")
def root():
    return {"Hello~~Hello~~Hello~~Hello~~": "no"}


@app.get("/items/{item_id}")
def item(item_id: int):
	return {"item_id: ": item_id}


@app.post("/register")
def register_item(item: Item):
	dicted_item: dict[str, bool] = dict(item)
	dicted_item['success'] = True
	
	return JSONResponse(dicted_item)


@app.put("/update")
def update_item(item: Item):
	dicted_item = {k:v for k, v in dict(item).items()}
	dicted_item['success'] = True

	return JSONResponse(dicted_item)