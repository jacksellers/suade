import sqlite3
import pandas as pd

con = sqlite3.connect("app.db")

for filename in ['commissions', 'order_lines', 'orders',
                 'product_promotions', 'products', 'promotions']:
    # load data
    df = pd.read_csv('app/data/{}.csv'.format(filename))
    # strip whitespace from headers
    df.columns = df.columns.str.strip()
    # drop data into database
    df.to_sql(filename, con)

con.close()