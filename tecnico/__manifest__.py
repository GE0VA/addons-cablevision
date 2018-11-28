# -*- coding: utf-8 -*-
{
    'name': "Modulo de Técnicos",

    'summary': """
        Ejercicio 1""",

    'description': """
        Modulo para probar los conocimientos adquiridos
    """,

    'author': "Delfix",
    'website': "http://www.delfix.com",
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','mail','portal'],

    # always loaded
    'data': [
        'views/tecnico_view.xml',
        'views/licencias_view.xml',
        'views/certificaciones_view.xml',
        'views/vehicles_view.xml',
        'data/cron.xml',
        'data/mail_template.xml',
        'security/security.xml',
        'security/ir.model.access.csv',
        'wizard/tecnico_wizard.xml',
    ],
}