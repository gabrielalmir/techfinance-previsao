import os
import pandas as pd
import psycopg2
from dotenv import load_dotenv

load_dotenv()

def get_db_connection():
    """Estabelece e retorna uma conexão com o banco de dados."""
    try:
        conn = psycopg2.connect(
            host=os.getenv("DB_HOST"),
            port=os.getenv("DB_PORT"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASS"),
            dbname=os.getenv("DB_NAME")
        )
        return conn
    except psycopg2.OperationalError as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
        raise

def fetch_sales_data() -> pd.DataFrame:
    """
    Busca e processa os dados de vendas do banco de dados PostgreSQL
    para prepará-los para o Prophet.
    """
    print("Buscando dados de vendas do banco de dados...")
    try:
        conn = get_db_connection()
        query = """
        SELECT
            data_emissao::date as ds,
            SUM(CAST(REPLACE(total, ',', '.') AS numeric)) as y
        FROM
            public.fatec_vendas
        GROUP BY
            data_emissao
        ORDER BY
            data_emissao;
        """
        df = pd.read_sql_query(query, conn)
        conn.close()

        print(f"Foram encontrados {len(df)} registros de vendas diárias.")

        if df.empty:
            return pd.DataFrame({'ds': pd.Series(dtype='datetime64[ns]'), 'y': pd.Series(dtype='float64')})

        df['ds'] = pd.to_datetime(df['ds'])

        return df
    except (Exception, psycopg2.Error) as error:
        print(f"Erro ao buscar dados do PostgreSQL: {error}")
        return pd.DataFrame({'ds': pd.Series(dtype='datetime64[ns]'), 'y': pd.Series(dtype='float64')})
