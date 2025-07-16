FROM python:3.11-slim

WORKDIR /app

# Install uv
RUN pip install --upgrade pip uv

# Copy project files
COPY pyproject.toml ./
COPY src ./src

# Build arg to control dev/prod install
ARG INSTALL_DEV=false

# Install dependencies
RUN if [ "$INSTALL_DEV" = "true" ]; then \
      uv sync --extra dev; \
    else \
      uv sync; \
    fi

EXPOSE 8000

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]