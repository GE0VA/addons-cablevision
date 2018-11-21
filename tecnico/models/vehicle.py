# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Vehiculos(models.Model):
    _name = 'vehicle'
    _description = 'Tabla para registrar Vehiculos'

    name = fields.Char(string='Nombre')
    description = fields.Text(string="Descripción", required=False, )
    placa = fields.Char(string="Placa", required=False, )
    # 2 -PARTE---------------------------------------------------------------------------------------------------------
    proper_license = fields.Many2one(comodel_name="licencias", string="Licencia para Este vehiculo", required=False, )
    # 2 -PARTE---------------------------------------------------------------------------------------------------------