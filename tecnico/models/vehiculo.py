# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Vehiculo(models.Model):
    _name = 'vehiculo.odoo'  # se crea la tabla campos_odoo

    name = fields.Char(string="Nombre", required=True, )
    description = fields.Text(string="Descripcion", required=False, )
    placa = fields.Char(string="Placa", required=True, )