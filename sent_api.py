from fastapi import FastAPI
from transformers import pipeline

app = FastAPI()
classifier = pipeline("sentiment-analysis")

@app.get("/predict/")
def predict():
    return classifier("I like machine learning engineering!")[0]
