# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Titulo(models.Model):
    _name = 'titulo.odoo'   # se crea la tabla campos_odoo
    _description="Titulos de los tecnicos"

    name = fields.Char(string="Nombre de titulo", required=False, )
    date = fields.Date(string="Fecha titulo", required=False, )
    color = fields.Integer(string="Color", required=False, )