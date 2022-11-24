import pandas as pd
import numpy as np
def load_and_process(url_or_path_to_csv_file):
    df1 = (pd.read_csv(url_or_path_to_csv_file)
      .pipe(lambda x: x.replace({'\$': '', ',': '', '%': '', '\(':'', '\)':'',}, regex=True))
      .replace('-', np.nan).dropna(subset=['revenues', 'revenue_percent_change', 'profits','profits_percent_change', 'assets', 'market_value',     'employees']))
    df2 = (df1.assign(price_to_earnings_ratio = lambda x: x['market_value'].astype(float)/x['profits'].astype(float))
          .assign(profit_margin = lambda x: x['profits'].astype(float)/x['revenues'].astype(float)))
    
    flt_cols = [x for x in df2.columns if df2.dtypes[x] != 'float64']
    flt_cols.remove('name')
    for i in flt_cols:
        df2[i] = df2[i].astype('float64')
        
    cols = df2.columns.tolist()
    cols = cols[0:3] + [cols[4]] + cols[-1:] + [cols[3]]  + cols[5:8] + [cols[10]] + [cols[9]] + [cols[8]]
    df2 = df2[cols]

    return df2