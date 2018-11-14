# -*- coding: utf-8 -*-

from odoo import models, fields, api



class Vehiculos(models.Model):
    _name = 'vehiculos.odoo'
    name = fields.Char(string='Nombre', required=True)
    description = fields.Text(string="Descripción", required=False)
    placa = fields.Char(string="Placa", required=False, )