#
import glob
import pandas as pd
import requests

from bs4 import BeautifulSoup
from vars import url, exchange_rate


def extract():

    # create an empty data frame to hold extracted data  
    df = pd.DataFrame(columns=["Name","MC_USD_Billion"])

    exchange_rate_df = pd.read_csv(exchange_rate)
    # print(exchange_rate_df)
    html_page = requests.get(url).text
    data = BeautifulSoup(html_page, 'html.parser')
    tables = data.find_all('tbody')
    rows = tables[0].find_all('tr') 
    for row in rows:
        col = row.find_all('td')
        if len(col)!= 0:
            data_dict = {"Name": str(col[1].find_all('a')[1]['title']),
                         "MC_USD_Billion": float(col[2].contents[0][:-1])}
            df1 = pd.DataFrame(data_dict, index=[0])
            df = pd.concat([df,df1], ignore_index=True)
    print(df)
    return df, exchange_rate_df
