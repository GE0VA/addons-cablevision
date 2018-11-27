# -*- coding: utf-8 -*-

from odoo import models, fields, api

class vehiculos(models.Model):
     _name = 'vehiculos.odoo'

     name = fields.Char(string="Nombre", required=True)
     description = fields.Char(string="Descripcion")
     placa = fields.Char(string="Placa", required=False)
     proper_license = fields.Many2one(comodel_name="licencias.odoo", string="Licencia para este vehículo", required=False)