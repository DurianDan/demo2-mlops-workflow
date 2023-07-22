# this Dockerfile is copied from the sample solution from the Judges

FROM python:3.10.11-bullseye

WORKDIR /mlflow/

# the context for building this file has been set to the parent folder, by the docker-compose.yaml file
COPY ./deployment/pip_requirements/mlflow.requirements.txt /mlflow/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /mlflow/requirements.txt
