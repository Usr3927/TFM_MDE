# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.addons.etl_launcher.ETL.ETL import stg_load
from odoo.addons.etl_launcher.ETL.ETL import ods_load

class etl_ondemand(models.Model):
  _name = 'etl_launcher.etl_ondemand'
  _description = 'ETL launcher'
  def onDemandLoad (self, context=None): 
    print("ETL started")
    stg_load()
    ods_load()
