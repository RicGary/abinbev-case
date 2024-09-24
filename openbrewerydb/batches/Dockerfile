FROM python:3.11-slim

WORKDIR /app

COPY batches/import_raw_data.py /app
COPY openbrewery.py /app

COPY batches/requirements.txt .
RUN pip install -r requirements.txt

ENTRYPOINT ["python", "import_raw_data.py"]
