import pandas as pd
from sqlalchemy import create_engine
data = pd.read_csv("data.csv", encoding = 'ISO-8859-1')
engine = create_engine('postgresql://postgres:postgres@db:5432/postgres')
data.to_sql('ecommerce', engine, method='multi')
input("Press Enter to continue...")