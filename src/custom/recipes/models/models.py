# -*- coding: utf-8 -*-

#from odoo import models, fields, api


#class recipes(models.Model):
#  _name = 'recipes.recipes'
#  _description = 'Modelo de módulo de recetas.'

#  receipt = fields.Char(string='Receta')
#     value2 = fields.Float(compute="_value_pc", store=True)
#  description = fields.Text(string='Descripción')
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
