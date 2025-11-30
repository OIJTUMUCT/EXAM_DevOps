from typing import List

import joblib
import numpy as np
import pandas as pd

from .config import MODEL_PATH, TARGET_NAMES
from .schemas import IrisSample, PredictItem


def load_model():
    # загрузка обученной модели RandomForest из models/model.pkl.

    if not MODEL_PATH.exists():
        raise RuntimeError(f"Файл модели не найден: {MODEL_PATH}")
    model = joblib.load(MODEL_PATH)
    return model


# глобальный экземпляр модели, чтобы не загружать её на каждый запрос
model = load_model()


def samples_to_dataframe(samples: List[IrisSample]) -> pd.DataFrame:
    # преобразуем список объектов IrisSample в DataFrame с теми же колонками,
    # которые использовались в scripts/ml_pipeline.py при обучении.
    rows = []
    for s in samples:
        rows.append(
            {
                "sepal length (cm)": s.sepal_length_cm,
                "sepal width (cm)": s.sepal_width_cm,
                "petal length (cm)": s.petal_length_cm,
                "petal width (cm)": s.petal_width_cm,
            }
        )
    df = pd.DataFrame(rows)
    return df


def predict_samples(samples: List[IrisSample]) -> List[PredictItem]:
    # бизнес-логика: принять батч IrisSample, вернуть список предсказаний.
    df = samples_to_dataframe(samples)
    preds = model.predict(df)
    preds = np.asarray(preds, dtype=int)

    result: List[PredictItem] = []
    for p in preds:
        class_id = int(p)
        class_name = TARGET_NAMES[class_id]
        item = PredictItem(class_id=class_id, class_name=class_name)
        result.append(item)

    return result