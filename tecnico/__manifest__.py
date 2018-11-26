# -*- coding: utf-8 -*-
{
     'name': "Tecnico",

    'summary': """
     Modulo para ver campos de Odoo
    """,

    'description': """
        Este modulo permite relizar el control de los tecnico
    """,

    'author': "Cable Vision",
    'website': "https://www.cablevision.cr/",
    'category': 'Uncategorized',
    'version': '0.1',
    'depends': ['base','mail','portal'],

    'data': [

        'views/tecnico_view.xml',
       # 'views/vehiculo_view.xml'
    ],
}