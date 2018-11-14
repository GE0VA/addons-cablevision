# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Licencias(models.Model):
    _name = 'licencias.odoo'
    _description = "licencias de técnicos"

    name = fields.Char(string="Nombre de la licencias", required=True, )
    descripcion = fields.Text(string="descripcion", required=False, )
