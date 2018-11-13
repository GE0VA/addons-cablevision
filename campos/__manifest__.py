# -*- coding: utf-8 -*-
{
    'name': "Campos",
    'summary': """
       Modulo para ver campos de Odoo
       """,
    'description': """
       Este modulo sera para montar los campos del sistema odoo
    """,
    'author': "Delfix",
    'website': "http://www.delfix.com",
    'category': 'Uncategorized',
    'version': '0.1',
    'depends': ['base','sale'],
    'data': [
        # 'security/ir.model.access.csv',
        'views/campos_view.xml',
        'data/campos.odoo.csv',
        'data/data.xml',
    ],

}