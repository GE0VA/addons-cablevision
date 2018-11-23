# -*- coding: utf-8 -*-
{
    'name': "Factura electronica",

    'summary': """
        Modulo de practica""",

    'description': """
        Practica de odoo para refresca info
    """,

    'author': "Cable Vision",
    'website': "cablevision.cr",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/11.0/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'account_invoicing'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/inherit_fact.xml',
    ]
}