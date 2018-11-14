from odoo import models, api, fields
class Vehiculos (models.Model):
    _name="vehiculos.oodo"
    name = fields.Char(string="Nombre", required=False, )
    placa = fields.Char(string="Placa", required=False, )
    description = fields.Text(string="Descripcion", required=False, )
