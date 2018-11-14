from odoo import fields, api, models

class Titulo(models.Model):
    _name='titulo.odoo'
    _description='Titulos de tecnicos'
    name = fields.Char(string="Nombre de Titulo", required=False, )
    fecha = fields.Date(string="Fecha de Titulo", required=False, )
    color = fields.Integer(string="Color", required=False, )