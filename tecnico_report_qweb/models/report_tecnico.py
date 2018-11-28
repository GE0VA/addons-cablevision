# -*- encoding: utf-8 -*-
from odoo import models, fields, api

class ReportTecnico(models.Model):
    _inherit = 'tecnico'

    @api.multi
    def get_user(self):
        return self.env.user.name