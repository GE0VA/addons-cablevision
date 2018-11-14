# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Certificaciones(models.Model):
    _name = 'certificaciones.odoo'
    _description = 'Certificaciones de los técnicos'
    name = fields.Char(string="Nombre de la certificación", required=True, )
    description = fields.Text(string="Descripción", required=False)
    date = fields.Date(string="Fecha", required=False)