from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
	return {"Hello~~Hello~~Hello~~Hello~~": "no"}


def item(item_id: int, q: Union[str, None] = None):
	return {"item_id: ": item_id, "q": q}
