# -*- coding: utf-8 -*-
{
    'name': "Campos Gabriel",

    'summary': """
        Son campos de ejemplo para la capacitación cable vision""",

    'description': """
        Esta es una larga definición de los campos realizados para cable vision 
    """,

    'author': "Delfix",
    'website': "http://www.delfixcr.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
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
        'data/data.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}