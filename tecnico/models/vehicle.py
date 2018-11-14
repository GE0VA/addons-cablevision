# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Vehiculos(models.Model):
    _name = 'vehicle'
    _description = 'Tabla para registrar Vehiculos'

    name = fields.Char(string='Nombre')
    description = fields.Text(string="Descripción", required=False, )
    placa = fields.Char(string="Placa", required=False, )