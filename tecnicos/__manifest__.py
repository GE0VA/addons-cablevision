# -*- coding: utf-8 -*-
{
    'name': "Control de técnicos",

    'summary': """
        Técnicos y su control""",

    'description': """
        El proposito de este módulo es controlar a los técnicos
    """,

    'author': "Cable Visión",
    'website': "http://www.cablevision.cr",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/11.0/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.2',

    # any module necessary for this one to work correctly
    'depends': ['base', 'mail'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/tecnicos_view.xml',
        'data/cron.xml',
        'security/security.xml',
        'security/ir.model.access.csv',
        'wizard/wizard_tecnico.xml'
    ],
}