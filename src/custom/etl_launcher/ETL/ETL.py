import pyodbc
import pandas as pd
import sqlalchemy as sqla

startdt=pd.to_datetime("today", utc=True)

# Specifying the ODBC driver, server name, database, etc. directly
orgn = sqla.create_engine("postgresql+psycopg2://odoo:odoo@localhost/odoo")
dstn = sqla.create_engine("postgresql+psycopg2://dwh:dwh@172.31.25.84/dwh")
sqls = [
  ["SELECT * FROM PRODUCT_TEMPLATE;", 'stg_product_template']
]
def stg_load_table(sql):
  data = pd.read_sql(sql[0],orgn)
  data['etl_load'] = startdt
  data.to_sql(sql[1], con=dstn, index=False, if_exists="append", schema='stg')

def stg_load():
  for sql in sqls:
    stg_load_table(sql)
