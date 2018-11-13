# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Campos(models.Model):
    _name = 'campos.odoo'
    name = fields.Char(string="Nombre", required=True ) #campo para el titulo del elemento
    active = fields.Boolean(string="Activo", help="Esta es la fila del campo" ) #campo con esto oculta el elemento en la lista
    description = fields.Text(string="Información del elemento", required=False )
    age = fields.Integer(string="Edad", required=True )
    page_test = fields.Html(string="Crear página" )
    photo = fields.Binary(string="Fotografia" )
    state = fields.Selection(string="Color", selection=[('azul', 'Azul'), ('rojo', 'Rojo'), ], required=False )
    date = fields.Date(string="Fecha registro", required=False, )
    date_time = fields.Datetime(string="Fecha ultimo ingreso", required=False, )

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