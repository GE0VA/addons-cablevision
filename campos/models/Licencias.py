from odoo import fields, api, models

class Licencias(models.Model):
    _name='licencias.odoo'
    _description='Licencias del tecnico'
    name = fields.Char(string="Tipo Licencia", required=False, )
    description = fields.Text(string="Descripcion", required=False, )
