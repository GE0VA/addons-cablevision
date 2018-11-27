# -*- coding: utf-8 -*-

from odoo import models, fields, api

class licencias(models.Model):
     _name = 'licencias.odoo'

     name = fields.Char( string="Nombre", required=True )
     description = fields.Char( string="Descripcion" )