import os
import pandas as pd
from sqlalchemy import create_engine

# 1. Extract
def extract(path='data/input.csv'):
    df = pd.read_csv(path)
    return df

# 2. Transform
def transform(df):
    df['date'] = pd.to_datetime(df['date'])
    df['total'] = df['quantity'] * df['price']
    return df

# 3. Load
def load(df, mysql_uri=None):
    if not mysql_uri:
        mysql_uri = os.environ.get('MYSQL_URI')
    if not mysql_uri:
        raise ValueError("No MYSQL_URI provided (env MYSQL_URI o argument).")
    engine = create_engine(mysql_uri)
    df.to_sql('sales_staging', con=engine, if_exists='append', index=False)

if __name__ == "__main__":
    df = extract()
    print("Extracted rows:", len(df))

    df = transform(df)
    print("Transformed sample:")
    print(df.head())

    # Per carregar a MySQL (quan tinguis la BD activa amb Docker Compose):
    # load(df)
    # print("Loaded data to MySQL")