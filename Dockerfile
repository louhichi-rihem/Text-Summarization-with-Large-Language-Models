FROM python:3.9-slim

# Set working directory inside the container
WORKDIR /app

# Copy application files to the container
COPY summarization.py /app/
COPY requirements.txt /app/
COPY bart_finetuned_samsum/ /app/model/

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose Streamlit's default port
EXPOSE 8501

# Run the application
CMD ["streamlit", "run", "summarization.py", "--server.port=8501", "--server.enableCORS=false"]