# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Certificaciones(models.Model):
    _name = 'certificaciones'
    _description = 'Tabla certificaciones'

    name = fields.Char(string='Nombre')
    description = fields.Text(string="Descripción", required=False, )
    date_curse = fields.Datetime(string="Fecha de Certificación", required=False, )