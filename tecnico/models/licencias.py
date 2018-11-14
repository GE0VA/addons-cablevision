# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Licencias(models.Model):
    _name = 'licencias'
    _description = 'Tabla para registrar tecnicos'

    name = fields.Char(string='Nombre')
    description = fields.Text(string="Descripción", required=False, )
    
   