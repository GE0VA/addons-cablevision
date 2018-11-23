# -*- coding: utf-8 -*-

from odoo import models, fields, api

class InheritTecnicos(models.Model):
     _inherit = 'tecnicos.odoo'

     calle1 = fields.Char( string="Calle 1" )
     ciudad = fields.Char( string="Ciudad" )
     provincia = fields.Many2one( comodel_name="res.country.state", string="Provincia" )
     pais = fields.Many2one( comodel_name="res.country", string="Pais" )
     active = fields.Boolean( string="Activo"  )

#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100