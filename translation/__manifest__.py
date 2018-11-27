# -*- coding: utf-8 -*-
{
    'name': "Translation Práctica",

    'summary': """
        Módulo de práctica para traducción""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Andrés Garita",
    'website': "https://cablevision.cr",

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
        'views/product_view.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}