from fastapi import FastAPI
from pydantic import BaseModel
from app.model.model import predict_pipeline
from app.model.model import __version__ as model_version

app = FastAPI()

class textInput(BaseModel):
	text : str


class predictOutput(BaseModel):
	language : str


@app.get('/')
def home():
	return {"Health Check" : "OK", "Version" : model_version}


@app.post('/predict', response_model=predictOutput)
def predict(payload : textInput):
	language = predict_pipeline(payload.text)
	return {"language" : language}

