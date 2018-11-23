# -*- coding: utf-8 -*-

from odoo import models, fields, api

class InheritFact(models.Model):
    _inherit = 'account.invoice'

    llave_cripto = fields.Binary( string="Llave criptografica" )
    usuario = fields.Char( string="Usuario de factura electronica" )
    contrasena = fields.Char( string="Contrasena de factura electronica" )
    pin = fields.Char( string="Pin", size=4 )
    num_electro = fields.Char( string="Numero electronico", readonly=True, store=False )

#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100