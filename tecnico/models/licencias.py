# -*- coding: utf-8 -*-

from odoo import models, fields, api



class Licencias(models.Model):
    _name = 'licencias.odoo'
    name = fields.Char(string='Nombre', required=True)
    description = fields.Text(string="Descripción", required=False)