import redis
from fastapi import FastAPI
from pydantic import BaseModel
from app.model.model import predict_pipeline
from app.model.model import __version__ as model_version

app = FastAPI()
r = redis.Redis(host="redis", port=6379)

class textInput(BaseModel):
	text : str

class predictOutput(BaseModel):
	language : str


@app.get('/')
def home():
	return {"Health Check" : "OK", "Version" : model_version}


@app.get('/unique')
def unique():
	r.incr("Unique")
	return {"Unique" : r.get("Unique")}


@app.post('/predict', response_model=predictOutput)
def predict(payload : textInput):
	language = predict_pipeline(payload.text)
	return {"language" : language}

