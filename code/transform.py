def transform(data, exchange_rate_df):
    data['MC_GBP_Billion'] = data.MC_USD_Billion.astype(float).mul(
        exchange_rate_df.loc[exchange_rate_df['Currency']=='GBP', 'Rate'].iloc[0]).round(2)
    data['MC_EUR_Billion'] = data.MC_USD_Billion.astype(float).mul(
        exchange_rate_df.loc[exchange_rate_df['Currency']=='EUR', 'Rate'].iloc[0]).round(2)
    data['MC_INR_Billion'] = data.MC_USD_Billion.astype(float).mul(
        exchange_rate_df.loc[exchange_rate_df['Currency']=='INR', 'Rate'].iloc[0]).round(2)
    return data