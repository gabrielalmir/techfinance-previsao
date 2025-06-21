# Use uma imagem base Python oficial e leve.
FROM python:3.10-slim

# Instale as dependências de sistema necessárias para Prophet e psycopg2.
# 'build-essential' é para compilar pacotes e 'libpq-dev' para a conexão com PostgreSQL.
RUN apt-get update && apt-get install -y build-essential libpq-dev && rm -rf /var/lib/apt/lists/*

# Defina o diretório de trabalho no contêiner.
WORKDIR /app

# Copie o arquivo de dependências primeiro para aproveitar o cache do Docker.
COPY requirements.txt .

# Instale as dependências do Python.
# Usamos --no-cache-dir para manter o tamanho da imagem menor.
RUN pip install --no-cache-dir -r requirements.txt

# Copie o restante do código da aplicação para o diretório de trabalho.
COPY . .

# Exponha a porta em que a aplicação será executada.
EXPOSE 8000

# Comando para executar a aplicação quando o contêiner for iniciado.
# O host 0.0.0.0 torna a aplicação acessível de fora do contêiner.
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
