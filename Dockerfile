# install operation app (python , php , ...)
FROM python:3.12-alpine

# set env
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# set default directory
WORKDIR /app

# copy requirements to app folder < . > is default folder
COPY requirements.txt /app/

# update pip to last verison
RUN python -m pip install --upgrade pip

# install package > requirements.txt
RUN pip install -r requirements.txt

# copy all dir to app
COPY . .