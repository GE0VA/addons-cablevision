# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Vehiculos(models.Model):
    _name = 'vehiculos.odoo'
    _description = "Vehiculos"

    name = fields.Char(string="Nombre del Vehiculo", required=True, )
    description = fields.Text(string="Description", required=False, )
    placa = fields.Char(string="Placa", required=False, )
