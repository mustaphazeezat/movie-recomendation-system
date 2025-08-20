# Use official Python image as base
FROM python:3.10-slim

# Set working directory
WORKDIR /code

# Copy requirements file if exists
COPY requirements.txt  /code/requirements.txt

# Install dependencies
RUN pip install --no-cache-dir -r /code/requirements.txt

# Copy project files
COPY ./app /code/app

# Copy correlation matrix
COPY ./app/corr_matrix_sparse.joblib /code/app/corr_matrix_sparse.joblib
# Expose port (change if your app uses a different port)
EXPOSE 8000

# Set default command (adjust as needed)
CMD ["uvicorn", "app.app:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]