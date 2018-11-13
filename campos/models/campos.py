# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Campos(models.Model):
    _name = 'campos.odoo'
    name = fields.Char(string="", required=False, )
    active = fields.Boolean(string="Activo",default=True  )




# class campos(models.Model):
#     _name = 'campos.campos'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100