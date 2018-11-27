# -*- encoding: utf-8 -*-
{
    "name": "Reporte de Técnicos QWeb",
    "version": "0.1",
    "author": "Delfix",
    "website": "http://www.delfixcr.com",
    "category": "Report",
    "description": """
    Reportes de Tecnicos
""",
    "depends": ['base','tecnico'],
    'data': [
        'security/security.xml',
        'reports/tecnico_report.xml',
        'reports/header_inherit_report.xml',
        'data/paper_format.xml',
        'wizard/wizard_tecnico_report_view.xml',
    ],
}
