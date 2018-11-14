# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Titulo(models.Model):
     _name = 'titulo.odoo'
     _description = "Titulos de Tecnicos"
     
     name = fields.Char(string="Nombre de Titulo", required=False, )
     date = fields.Date(string="Fecha Titulo", required=False, )
     color = fields.Integer(string="Color", required=False, )
