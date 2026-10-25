FROM python:3.8-slim
LABEL authors="Csernák Hunor"
LABEL description="Demonstációs példa sérülékeny OpenCV és request könyvtárak használatával Pythonban"
LABEL version="1.0"

WORKDIR /app

RUN apt-get update && apt-get install -y \
    libglib2.0-0 \
    libsm6 \
    libxext6 \
    libxrender-dev \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY demo.py .

ENTRYPOINT ["python", "demo.py"]