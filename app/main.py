from fastapi import FastAPI

from .api import router as api_router


app = FastAPI(
    title="Iris RandomForest API (HW5 CI/CD)",
    version="1.0.0",
    description=(
        "FastAPI-сервис для инференса модели RandomForest, обученной на датасете Iris. "
        "Модель тренируется скриптом scripts/ml_pipeline.py и сохраняется в models/model.pkl. "
        "Пайплайн запускается в CI, а API может быть упаковано в контейнер и задеплоено через Terraform."
    ),
)


# Подключаем роутер с эндпоинтами
app.include_router(api_router)