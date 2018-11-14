# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Titulos(models.Model):
    _name = 'titulos.odoo'
    _description = 'Titulos obtenidos'

    name = fields.Char( string="Nombre del titulo", required=True )
    date = fields.Date( string="Fecha de conclusión" )
    color = fields.Integer( string="Color" )