import pandas as pd
import numpy as np
def load_and_process(url_or_path_to_csv_file):
    df1 = (pd.read_csv(url_or_path_to_csv_file)
      .pipe(lambda x: x.replace({'\$': '', ',': '', '%': '', '\(':'', '\)':'',}, regex=True))
      .replace('-', np.nan).dropna(subset=['revenues', 'revenue_percent_change', 'profits','profits_percent_change', 'assets', 'market_value',     'employees'])).astype({'revenues': 'float', 'revenue_percent_change': 'float', 'profits': 'float','profits_percent_change': 'float', 'assets': 'float', 'market_value': 'float', 'employees': 'float'});
    df2 = (df1.assign(revenue_over_profit = lambda x: x['revenues'].astype(float)/x['profits'].astype(float))
      .assign(market_over_asset = lambda x: x['market_value'].astype(float)/x['assets'].astype(float)))
    return df2
