# app/schemas.py
from typing import List

from pydantic import BaseModel


class IrisSample(BaseModel):
    #одна строка данных Iris для инференса.
    
    sepal_length_cm: float
    sepal_width_cm: float
    petal_length_cm: float
    petal_width_cm: float


class PredictRequest(BaseModel):
    # батч из нескольких объектов для инференса.

    samples: List[IrisSample]


class PredictItem(BaseModel):
    # одно предсказание модели.

    class_id: int
    class_name: str


class PredictResponse(BaseModel):
    # ответ API на запрос /predict.

    predictions: List[PredictItem]