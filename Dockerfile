FROM python:3.8

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /code

# Install Dependencies
COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

# Copy project
COPY . /code/

CMD ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "80"]
