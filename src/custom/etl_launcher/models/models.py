# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.addons.etl_launcher.ETL.ETL import stg_load

class etl_schedule(models.Model):
  _name = 'etl_launcher.etl_schedule'
  _description = 'Lanzador de la ETL'
  name = fields.Char(string="Nombre")
  fecha = fields.Datetime(string='Fecha y hora', required=True, readonly=False, default=fields.Datetime.now())
  description = fields.Text(string='Descripción')

  def onDemandLoad (self, context=None): 
    print("ETL started")
    stg_load()
