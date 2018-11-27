# -*- coding: utf-8 -*-

from odoo import models, fields, api


class InherentTecnico(models.Model):
    _name = 'tecnico.odoo'

    calle1 = fields.Char(string="Calle 1", required=False, )
    ciudad = fields.Char(string="Ciudad", required=False, )
    pais = fields.Many2one(comodel_name="res.country", string="Pais", required=False, )
    provincia = fields.Many2one(comodel_name="res.country.state", string="Provincia", required=False, )
    active = fields.Boolean(string='Activo')

# class inherit_tecnico(models.Model):
#     _name = 'inherit_tecnico.inherit_tecnico'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100