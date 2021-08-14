# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError


class ProductTemplate(models.Model):
  _inherit = 'product.template'
  ingredient_id = fields.Many2many('product.template', relation='template_recipe_rel' ,column1="template_id", column2="ingredient_id", string='Ingredientes', help="Lista de ingredientes.")
  ingredient_ids = fields.Many2many('product.template', relation='template_recipe_rel' , column1="ingredient_id", column2="template_id" ,string='Platos')
  @api.constrains('ingredient_id')
  def _check_adding_itself(self):
    for ingrdnt in self.ingredient_id:
      if ingrdnt.id == self.id:
        raise ValidationError('No es posible crear recetas recursivas.')
#    for ingrdnts in self.ingredient_id:
#      raise ValidationError(ingrdnts.name)
#class recipes(models.Model):
#  _name = 'recipes.ingredients'
#  _description = 'Ingredientes por receta.'

#  ingredient = fields.Integer(string="Id. ingrediente", default=lambda self: self.env['ir.sequence'].next_by_code('increment_your_field'))
#  meal_id = fields.Many2one("product.template", string="Producto")
#  description = fields.Text(string='Descripción')
#  grams = fields.Float(string='Gramos')
#  litres = fields.Float(string='Litros')

#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
