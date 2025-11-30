from pathlib import Path
from sklearn.datasets import load_iris


ROOT_DIR = Path(__file__).resolve().parents[1]

# путь к сериализованной модели RandomForest, которую создаёт scripts/ml_pipeline.py
MODEL_PATH = ROOT_DIR / "models" / "model.pkl"

# метаданные датасета Iris
_iris_meta = load_iris()
TARGET_NAMES = list(_iris_meta.target_names)