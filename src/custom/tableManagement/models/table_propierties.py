# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models


class TablePropierties(models.Model):
    _name = "table.propierties"
    _description = "Table propierties."

    name = fields.Char('Table', required=True, translate=True)
    table_diners = fields.Integer('Diners', required=True, default=4)
