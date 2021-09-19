# -*- coding: utf-8 -*-
{
    'name': "Recetas",

    'summary': """
        Módulo de gestión de recetas.""",

    'description': """
        Este módulo permite crear recetas. Es necesario mantenerlo actualizado con el fin de controlar los recursos necesarios para elaborar los platos de la carta.
    """,

    'author': "TFM_MDE",
    'website': "https://www.tfm_mde.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Productivity/Recetas',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','point_of_sale', 'stock_account'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False
}
