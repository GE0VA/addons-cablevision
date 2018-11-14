# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Licencia(models.Model):
    _name = 'licencia.odoo'  # se crea la tabla campos_odoo

    name = fields.Char(string="Nombre", required=False, )
    description = fields.Text(string="Descripcion", required=False, )