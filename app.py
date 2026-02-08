from fastapi import FastAPI, Request, Response
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
import pickle
import pandas as pd
from pydantic import BaseModel

app = FastAPI()

#templates
templates = Jinja2Templates(directory="templates")


with open("diabet_predict_model_complete.pkl", "rb") as f:
    saved_data = pickle.load(f)
    model = saved_data["model"]
    encoders = saved_data["encoders"]



class DiabetesFeatures(BaseModel):
    Age : float
    Height : float
    Weight : float
    family_history : str
    FAVC : str
    FCVC : float
    CAEC : str
    CH2O : float
    SCC : str
    FAF : float
    TUE : float
    CALC : str
    MTRANS : str



@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})



@app.post("/predict")
async def predict(features: DiabetesFeatures):
    input_data = pd.DataFrame([features.model_dump()])

    # Encode categorical columns
    for col in ['CAEC', 'CALC', 'MTRANS', 'family_history', 'FAVC', 'SCC']:
        input_data[col] = encoders[col].transform(input_data[col].astype(str))

    # Ensure column order matches model's training data
    if hasattr(model, 'feature_names_in_'):
        input_data = input_data[[c for c in model.feature_names_in_ if c in input_data.columns]]

    prediction = model.predict(input_data)
    result = prediction[0]

    # Convert numpy types to native Python for JSON serialization
    if hasattr(result, 'item'):
        result = result.item()
    else:
        result = str(result)

    return {"prediction": result}


