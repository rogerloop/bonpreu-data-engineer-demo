import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import pandas as pd
from etl.etl_main import extract, transform

def test_extract():
    df = extract("data/input.csv")
    assert not df.empty
    assert all(col in df.columns for col in ["date", "product", "quantity", "price"])

def test_transform():
    df = pd.DataFrame({
        "date": ["2025-01-01"],
        "product": ["Pa"],
        "quantity": [10],
        "price": [1.20]
    })
    df_transformed = transform(df)
    assert "total" in df_transformed.columns
    assert df_transformed["total"].iloc[0] == 12.0