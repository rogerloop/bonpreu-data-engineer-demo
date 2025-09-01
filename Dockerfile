# -----------------------------
# Etapa base: imatge oficial de Python
# -----------------------------
FROM python:3.10-slim

# Evitem que Python escrigui fitxers .pyc i assegurem output immediat
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# -----------------------------
# Instal·lar dependències del sistema
# -----------------------------
RUN apt-get update && apt-get install -y \
    build-essential \
    default-mysql-client \
    netcat-openbsd \
    && rm -rf /var/lib/apt/lists/*

# -----------------------------
# Crear directori de treball
# -----------------------------
WORKDIR /app

# -----------------------------
# Copiar fitxers de dependències primer (per cache)
# -----------------------------
COPY requirements.txt .

# Instal·lar dependències Python
RUN pip install --no-cache-dir -r requirements.txt

# -----------------------------
# Copiar la resta del projecte
# -----------------------------
COPY . .

# -----------------------------
# Executar script ETL per defecte
# -----------------------------
CMD ["python", "etl/etl_main.py"]