# -*- coding: utf-8 -*-

from odoo import models, fields, api

class InheritTecnico(models.Model):
    _inherit = 'tecnico'

    calle1 = fields.Char(string="Calle 1", required=False, )
    ciudad = fields.Char(string="Ciudad", required=False, )
    pais = fields.Many2one(comodel_name="res.country", string="País", required=False, )
    provincia = fields.Many2one(comodel_name="res.country.state", string="Provincia", required=False, )
    active = fields.Boolean(string="Activo",  )

    @api.onchange('licencia_id')
    def onchange_licencia_id(self):
        # super(InheritTecnico, self).onchange_licencia_id()
        self.age = ''
        self.name = ''