# -*- coding: utf-8 -*-

from odoo import models, fields, api



class Titulo(models.Model):
    _name = 'titulo.odoo'
    _description = 'Títulos de los técnicos'
    name = fields.Char(string="Nombre del Título", required=False, )
    date = fields.Date(string="Fecha", required=False)
    color = fields.Integer(string='Color', required=False)