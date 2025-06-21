import psycopg2
from dotenv import load_dotenv
import os
from fastapi import FastAPI, Depends, Query, HTTPException
from auth import verify_token
from database import fetch_sales_data
from forecasting import prever_vendas

# Load environment variables from .env
load_dotenv()

# Fetch variables
USER = os.getenv("DB_USER")
PASSWORD = os.getenv("DB_PASS")
HOST = os.getenv("DB_HOST")
PORT = os.getenv("DB_PORT")
DBNAME = os.getenv("DB_NAME")

app = FastAPI(
    title="API de Previsão e Otimização",
    description="Uma API para realizar previsões de séries temporais e otimizações.",
    version="0.1.0",
)

@app.get("/")
def read_root():
    return {"message": "Bem-vindo à API de Previsão"}

@app.post("/previsao/vendas")
def forecast_sales(
    dias_previsao: int = Query(30, description="Número de dias para prever no futuro."),
    auth: str = Depends(verify_token)
):
    """
    Endpoint para previsão de vendas.
    Busca dados reais do banco de dados, treina um modelo Prophet e retorna a previsão.
    """
    # 1. Buscar dados reais
    df_vendas = fetch_sales_data()

    if df_vendas.empty:
        raise HTTPException(status_code=404, detail="Nenhum dado de venda encontrado para realizar a previsão.")

    # 2. Fazer a previsão
    # A função de previsão espera colunas 'ds' e 'y', que já foram formatadas em fetch_sales_data
    forecast_df = prever_vendas(df_vendas, periodos=dias_previsao)

    # Converte o resultado para um formato JSON amigável
    forecast_df['ds'] = forecast_df['ds'].dt.strftime('%Y-%m-%d')

    return forecast_df.to_dict(orient='records')

# Connect to the database
try:
    connection = psycopg2.connect(
        user=USER,
        password=PASSWORD,
        host=HOST,
        port=PORT,
        dbname=DBNAME
    )
    print("Connection successful!")

    # Create a cursor to execute SQL queries
    cursor = connection.cursor()

    # Example query
    cursor.execute("SELECT NOW();")
    result = cursor.fetchone()
    print("Current Time:", result)

    # Close the cursor and connection
    cursor.close()
    connection.close()
    print("Connection closed.")

except Exception as e:
    print(f"Failed to connect: {e}")
