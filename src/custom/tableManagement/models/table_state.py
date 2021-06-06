# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models
from datetime import datetime


class TableState(models.Model):
    _name = "table.state"
    _description = "Table state over time."
#    _order = "sequence"

    table_id = fields.Many2one("table.propierties", string="Table id")
    table_state = fields.Selection([('0','Sentarse'),('1','1r plato'),('2','2º plato'),('3','3r plato'),('4','Postre')],'Table state', required=True, default='0')
    is_actual_state = fields.Boolean('Actual', required=True, default=True)
    starting_time = fields.Datetime('Starting time', required=True, default=datetime.today())   
    ending_time = fields.Datetime('Ending time', required=False)
