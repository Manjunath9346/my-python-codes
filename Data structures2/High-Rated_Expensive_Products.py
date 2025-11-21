def filter_high_rated_expensive(df):
    return df[
        (df["rating"] >= 4.5) &
        (df["quantity_in_stock"] > 0) &
        (df["price"] >= 300)
    ]
