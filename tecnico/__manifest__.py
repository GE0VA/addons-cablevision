# -*- coding: utf-8 -*-
{
    'name': "Tecnico",

    'summary': """
       Modulo para ver tecnicos
       """,

    'description': """
        Este modulo agrega los campos del tecnico en sistema odoo
    """,

    'author': "Cable vision",
    'website': "http://www.cablevision.com",

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
        'views/tecnico_view.xml',
    ],

}