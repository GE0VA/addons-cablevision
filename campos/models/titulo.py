# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Titulos(models.Model):
    _name = 'titulo.odoo'
    _description = "Titulos de técnicos"

    name = fields.Char(string="Nombre del titulo", required=True, )
    date = fields.Date(string="fecha", required=False, )
    color = fields.Integer(string="Color", required=False, )
    otrarelacion = fields.Integer(string="Color", required=False, )