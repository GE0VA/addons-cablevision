# -*- coding: utf-8 -*-

from odoo import models, fields, api

class WizardTecnico(models.TransientModel):
    _name = 'tecnico.wizard'
    
    user = fields.Many2one(comodel_name="res.users", string="Usuario a asignar", required=True, default=6 )
    date = fields.Date(string="Fecha a revisar", required=False,default="2018-10-25" )

    @api.multi
    def register_users(self):
        if self._context.get('active_ids',False):
            obj_tecnicos = self.env['tecnico'].browse(self._context.get('active_ids',False))
            for rec in obj_tecnicos:
                rec.date_revision = self.date
                rec.user = self.user.id
