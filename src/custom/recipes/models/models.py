# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError


class ProductTemplate(models.Model):
  _inherit = 'product.template'
  ingredient_id = fields.One2many('recipes.ingredient', inverse_name="meal_id", string='Ingrediente')
  
  @api.constrains('ingredient_id')
  def _check_adding_itself(self):
    for ingrdnt in self.ingredient_id:
      for prdct in ingrdnt.raw_id:
        if self.id == prdct.id :
          raise ValidationError('Los ingredientes del plato deben ser diferentes del propio plato. En el ingrediente "'+ingrdnt.name+'" se ha incluido el plato "'+prdct.name+'".')
    
class Ingredient(models.Model):
  _name = 'recipes.ingredient'
  _description = 'Ingredientes por receta.'
  name=fields.Char(string='Ingrediente')
  meal_id = fields.Many2one("product.template", string='Plato')
  raw_id = fields.Many2one('product.template',  string="Materia prima")
  description = fields.Text(string='Descripción')
  grams=fields.Float(string='Gramos')
  litres=fields.Float(string='Litros')
  
  @api.constrains('raw_id')
  def _check_null_product(self):
    if not self.raw_id:
      raise ValidationError('El ingrediente '+self.name+' debe relacionarse con una "Materia prima".')
		
#  @api.depends('value')
#  def _value_pc(self):
#   for record in self:
#     record.value2 = float(record.value) / 100
