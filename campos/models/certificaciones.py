# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Certificaciones(models.Model):
    _name = 'certificaciones.odoo'
    _description = "Certificaciones de técnicos"

    name = fields.Char(string="Nombre de la certificacion", required=True, )
    descripcion = fields.Text(string="descripcion", required=False, )
    color = fields.Integer(string="Color", required=False, )
    curso_date = fields.Datetime(string="Fecha del curso", required=False, )
