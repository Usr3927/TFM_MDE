import pyodbc
import pandas as pd
import sqlalchemy as sqla
import os

def get_query(file_path):
  f=open(file_path,"r")
  return f.read()
  

def stg_load_table(sql, conflict):
  data = pd.read_sql(sql[0],orgn)
  data['etl_load'] = startdt
  data.to_sql(sql[1], con=dstn, index=False, if_exists=conflict, schema='stg')

def ods_load_table(sql, conflict):
  data = pd.read_sql(sql[0],dstn)
  data['etl_load'] = startdt
  data.to_sql(sql[1], con=dstn, index=False, if_exists=conflict, schema='ods')

def stg_load():
  for sql in stg_sqls:
    stg_load_table(sql, "replace")

def ods_load():
  for sql in ods_sqls:
    ods_load_table(sql, "replace")

#Loading datetime start    
startdt=pd.to_datetime("today", utc=False)

#Specifying the ODBC driver, server name, database, etc. directly
orgn = sqla.create_engine("postgresql+psycopg2://odoo:odoo@localhost/odoo")
dstn = sqla.create_engine("postgresql+psycopg2://dwh:dwh@172.31.25.84/dwh")
#dstn = sqla.create_engine("postgresql+psycopg2://dwh:dwh@localhost/dwh")
root =os.environ['HOME']+r"/TFM_MDE/src/custom/etl_launcher/ETL/"
stg_sqls = [
  [get_query(root+"stg_product_template.sql"), 'stg_product_template'],
  [get_query(root+"stg_product_product.sql"), 'stg_product_product'],
  [get_query(root+"stg_product_supplierinfo.sql"), 'stg_product_supplierinfo'],
  [get_query(root+"stg_pos_order.sql"), 'stg_pos_order'],
  [get_query(root+"stg_pos_order_line.sql"), 'stg_pos_order_line'],
  [get_query(root+"stg_pos_session.sql"), 'stg_pos_session'],
  [get_query(root+"stg_res_partner.sql"), 'stg_res_partner'],
]
ods_sqls = [
  [get_query(root+"ods_fact_pos_sold.sql"), 'ods_fact_pos_sold'],
]
