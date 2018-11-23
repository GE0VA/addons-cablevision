# -*- coding: utf-8 -*-
{
    'name': "Herencias tecnicos",

    'summary': """
        Herencias""",

    'description': """
        Esto son herencias de los tecnicos para nuevos campos
    """,

    'author': "Cable Vision",
    'website': "http://www.cablevision.cr",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/11.0/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','tecnicos'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/inherit_tecnicos_view.xml'
    ]
}