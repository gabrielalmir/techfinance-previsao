import pandas as pd
from prophet import Prophet
from datetime import datetime

def prever_vendas(df_vendas: pd.DataFrame, periodos: int = 30) -> pd.DataFrame:
    """
    Utiliza o Prophet para prever as vendas futuras.

    :param df_vendas: DataFrame com os dados de vendas no formato do Prophet (ds, y).
    :param periodos: Número de dias no futuro para prever a partir de hoje.
    :return: DataFrame com os resultados da previsão, apenas para datas futuras.
    """
    if df_vendas.empty:
        print("Nenhum dado de venda encontrado para realizar a previsão.")
        return pd.DataFrame({
            'ds': pd.Series(dtype='datetime64[ns]'),
            'yhat': pd.Series(dtype='float64'),
            'yhat_lower': pd.Series(dtype='float64'),
            'yhat_upper': pd.Series(dtype='float64')
        })

    df_prophet = df_vendas.copy()
    df_prophet['ds'] = pd.to_datetime(df_prophet['ds'])

    # Instancia e treina o modelo
    model = Prophet(daily_seasonality='auto')
    model.fit(df_prophet)

    # Calcula o horizonte de previsão necessário para cobrir desde a última data
    # de dados até o fim do período de previsão desejado a partir de hoje.
    last_historic_date = df_prophet['ds'].max()
    today = pd.to_datetime(datetime.now().date())

    delta_days = 0
    if last_historic_date < today:
        delta_days = (today - last_historic_date).days

    total_periods_to_forecast = delta_days + periodos

    future = model.make_future_dataframe(periods=total_periods_to_forecast)
    forecast = model.predict(future)

    # Filtra o resultado para mostrar apenas as previsões a partir de hoje
    # e garante que o resultado tenha o número de períodos solicitados.
    future_forecast = forecast[forecast['ds'] >= today].copy()

    final_forecast = future_forecast.head(periodos)

    # Retorna as colunas relevantes da previsão
    return pd.DataFrame(final_forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']])
