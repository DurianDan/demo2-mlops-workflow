from fastapi import FastAPI
import mlflow
from os import getenv

mlflow.set_tracking_uri(getenv("MLFLOW_SERVER_TRACKING_URI"))

app = FastAPI()
