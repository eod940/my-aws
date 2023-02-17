from fastapi import FastAPI

my_fastapi_app = FastAPI()


@my_fastapi_app.get("/")
def root():
	return {"Hello~~"}
