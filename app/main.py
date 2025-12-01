from fastapi import FastAPI

from .api import router as api_router


app = FastAPI(
    title="Iris RandomForest API",
    version="1.0.0",
    description=(
        "FastAPI-сервис для инференса модели RandomForest, обученной на датасете Iris. "
        "Модель тренируется скриптом scripts/ml_pipeline.py и сохраняется в models/model.pkl. "
    ),
)


# Подключаем роутер с эндпоинтами
app.include_router(api_router)