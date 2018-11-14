# -*- coding: utf-8 -*-

from odoo import models, fields, api

class InheritTecnico(models.Model):
    _inherit = 'tecnico'

    calle1 = fields.Char(string="Calle 1", required=False, )
    ciudad = fields.Char(string="Ciudad", required=False, )
    pais = fields.Many2one(comodel_name="res.country", string="País", required=False, )
    provincia = fields.Many2one(comodel_name="res.country.state", string="Provincia", required=False, )
    active = fields.Boolean(string="Activo",  )