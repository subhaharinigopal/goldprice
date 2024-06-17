from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
import pickle


app = FastAPI()


origins = ["*"]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

model = pickle.load(open('gold_price_pred_model.pkl', 'rb'))


class goldPriceModel(BaseModel):
    spxFloat: float
    usoFloat: float
    slvFloat: float
    euroUSDRatioFloat: float


@app.get('/')
def welcome_msg():
    return {
        'success': True,
        'message': 'server of gold price prediction api is up and run successfully'
    }


@app.post('/pred-gold-price')
async def pred_price(valuesFromFrontend: goldPriceModel):

    spx = valuesFromFrontend.spxFloat
    uso = valuesFromFrontend.spxFloat
    slv = valuesFromFrontend.slvFloat
    eurousdratio = valuesFromFrontend.euroUSDRatioFloat

    pred_data = pd.DataFrame([[spx, uso, slv, eurousdratio]], columns=[
                             'SPX', 'USO', 'SLV', 'EUR/USD'])

    prediction = model.predict(pred_data)

    return {
        'success': True,
        'pred_result_value': float(prediction[0])
    }
