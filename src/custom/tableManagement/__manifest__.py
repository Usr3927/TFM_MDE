# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Table Management',
    'author': 'TFM_MDE',
    'version': '1.0',
    'category': 'Productivity/Table Management',
    'summary': 'Track the tables state.',
    'description': "Track the tables state.",
    'website': 'https://www.tfm_mde.com',
    'depends': [
        'base_setup',
        'web_tour',
    ],
    'data': [
        'security/ir.model.access.csv',
        'data/table_management_tables_views.xml',
        'views/table_management_menus.xml',
        'views/table_state_views.xml',
        'views/table_propierties_views.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False
}
