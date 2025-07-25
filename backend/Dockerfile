FROM continuumio/miniconda3

# Set working directory
WORKDIR /app

# Copy environment and install
COPY environment.yml .
RUN conda env create -f environment.yml

# Activate conda env and make sure it works in subprocesses
SHELL ["conda", "run", "-n", "music-rec-app-env", "/bin/bash", "-c"]

# Copy project files
COPY . .

# Optional: Activate environment and test
RUN conda run -n music-rec-app-env python --version

# Default command will be overridden by docker-compose
CMD ["streamlit", "run", "app/main.py"]
