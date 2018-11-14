# -*- coding: utf-8 -*-
{
    'name': "Campos",

    'summary': """
        Módulo para ver campos de Odoo""",

    'description': """
        Este módulo será para montar los campos del sistema Odoo
    """,

    'author': "Cable Visión",
    'website': "http://www.cablevision.cr",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/11.0/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/campos_view.xml',
        'data/campos.odoo.csv',
        # 'data/data.xml'
    ]
}