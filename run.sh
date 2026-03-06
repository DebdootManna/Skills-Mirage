#!/bin/bash
echo "Starting Skills Mirage Backend..."
# Hotfix for Python 3.14 Protobuf incompatibility
export PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION=python

# Run the scraper in the background
python -m backend.scraper &
SCRAPER_PID=$!

# Run the FastAPI server in the background
uvicorn backend.main:app --host 0.0.0.0 --port 8000 &
BACKEND_PID=$!

echo "Waiting for backend to initialize..."
sleep 3

echo "Starting Skills Mirage Frontend..."
# Run the Streamlit frontend
streamlit run frontend/app.py

# Cleanup on exit
trap "kill $SCRAPER_PID $BACKEND_PID" EXIT
