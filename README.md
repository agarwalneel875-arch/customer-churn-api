# Customer Churn Prediction API with FastAPI & Docker

## Overview

This project deploys a Machine Learning Customer Churn Prediction model using FastAPI and Docker.

The API accepts customer feature values and returns a churn prediction.

## Features

* FastAPI REST API
* Model inference endpoint
* Interactive Swagger UI documentation
* Dockerized deployment

## Project Structure

```text
.
├── app.py
├── model.pkl
├── requirements.txt
├── Dockerfile
├── README.md
└── Customer_Churn_API_Deployment.ipynb
```

## API Endpoints

### GET /

Returns API status.

### POST /predict

Returns customer churn prediction.

## Example Request

```json
{
  "feature1": 1,
  "feature2": 2,
  "feature3": 3,
  "feature4": 4
}
```

## Example Response

```json
{
  "prediction": 1
}
```

## Run Locally

```bash
pip install -r requirements.txt
python -m uvicorn app:app --reload
```

Open:

```text
http://127.0.0.1:8000/docs
```

## Docker

Build Image:

```bash
docker build -t churn-api .
```

Run Container:

```bash
docker run -p 8000:8000 churn-api
```

## Demo

Swagger UI and prediction screenshots are included in the repository.

