# -*- coding: utf-8 -*-

from odoo import models, fields, api


class licencias(models.Model):
    _name = 'licencias.odoo'
    _descripcion = 'Almacenara los vehiculos relacionados con el tecnico'

    name = fields.Char(string="Nombre licencia", required=False, )
    description_licencia = fields.Text(string="Descripcion licencia", required=False, )
