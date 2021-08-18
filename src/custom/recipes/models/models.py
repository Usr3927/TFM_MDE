# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError


class ProductTemplate(models.Model):
  _inherit = 'product.template'
  ingredient_id = fields.One2many('recipes.ingredient', inverse_name="meal_id", string='Ingrediente')
    
#  ingredient_id = fields.Many2many('product.template', relation='template_recipe_rel' ,column1="template_id", column2="ingredient_id", string='Ingredientes', help="Lista de ingredientes.")
#  ingredient_ids = fields.Many2many('product.template', relation='template_recipe_rel' , column1="ingredient_id", column2="template_id" ,string='Platos')
#  @api.constrains('ingredient_id')
#  def _check_adding_itself(self):
#    for ingrdnt in self.ingredient_id:
#      if ingrdnt.id == self.id:
#        raise ValidationError('No es posible crear recetas recursivas.')

class Ingredient(models.Model):
  _name = 'recipes.ingredient'
  _description = 'Ingredientes por receta.'
  name=fields.Char(string='Ingrediente')
  meal_id = fields.Many2one("product.template", string='Plato')
  raw_id = fields.Many2many('product.template', relation='template_recipe_rel', column1="template_id", column2="ingredient_id", string="Materia prima")
  description = fields.Text(string='Descripción')
  grams=fields.Float(string='Gramos')
  litres=fields.Float(string='Litros')
  
  _sql_constraints = [
    ('ingredient_name_unique', 'unique(name)', 'El ingrediente ya existe!')
]

  @api.constrains('meal_id')
  def _check_adding_itself(self):
    parent_id = self.env.context.get('parent_id') 
    parent_model = self.env.context.get('parent_model')  
#    raise ValidationError(parent_model)     

#  @api.depends('value')
#  def _value_pc(self):
#   for record in self:
#     record.value2 = float(record.value) / 100
