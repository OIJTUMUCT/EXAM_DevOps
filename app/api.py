from fastapi import APIRouter

from .schemas import PredictRequest, PredictResponse
from .services import predict_samples


router = APIRouter()


@router.get("/healthcheck")
async def healthcheck():
    # Healthcheck
    return {"status": "ok"}


@router.post("/predict", response_model=PredictResponse)
async def predict(request: PredictRequest) -> PredictResponse:
    # Эндпоинт для инференса: принимает батч примера и возвращает предсказания модели.
    predictions = predict_samples(request.samples)
    return PredictResponse(predictions=predictions)