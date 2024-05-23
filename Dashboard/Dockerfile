FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

# Kopjo skedarin CSV në imazhin Docker
COPY cleaned_data.csv /app/

CMD ["streamlit", "run", "Homepage.py"]
