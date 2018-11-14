# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Certificacion(models.Model):
    _name = 'certificacion.odoo'  # se crea la tabla campos_odoo

    name = fields.Char(string="Nombre", required=False, )
    description = fields.Text(string="Descripcion", required=False, )
    date = fields.Datetime(string="Fecha curso", required=False, )