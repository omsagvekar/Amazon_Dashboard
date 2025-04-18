# tests/test_app.py

import pandas as pd

def test_data_load():
    df = pd.read_csv("data/Amazonsales_cleaned.csv")
    assert not df.empty, "Dataset should not be empty"
    assert 'Order Date' in df.columns
    assert 'Sales' in df.columns
    assert 'Category' in df.columns

def test_order_date_parsing():
    df = pd.read_csv("data/Amazonsales_cleaned.csv")
    df['Order Date'] = pd.to_datetime(df['Order Date'], dayfirst=True, errors='coerce')
    assert df['Order Date'].notnull().any(), "All Order Dates are NaT — parsing failed"
    assert df['Order Date'].min().year >= 2000, "Earliest date should be reasonable (post-2000)"
