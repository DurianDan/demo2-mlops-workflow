FROM python:3.10.11-bullseye

WORKDIR /code

# the context for building this file has been set to the parent folder, by the docker-compose.yaml file
COPY ./deployment/pip_requirements/fastapi.requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# the code has been mounted to local folder instead of copy the whole project into the docker image
# COPY ./app /code/app


# this command should have been put into the docker-compose.yaml file for easy configuration.
# But because of error with docker-compose :v, it's here
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]


