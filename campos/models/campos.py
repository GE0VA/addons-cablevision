# -*- coding: utf-8 -*-

from odoo import models, fields, api



class Campos(models.Model):
    _name = 'campos.odoo'
    name = fields.Char(string="Nombre", required=False, )
    active = fields.Boolean(string="Activo", help='Esta es la ayuda del campo' )
    description = fields.Text(string="Descripcion", required=False, )
    html = fields.Html(string="Campo HTML",  )
    amount = fields.Float(string="Monto",  required=False, )
    age = fields.Integer(string="Age", required=False, )
    binary = fields.Binary(string="Binario",  )
    state = fields.Selection(string="Estado", selection=[
        ('borrador', 'Borrador'),
        ('validado', 'Validado'),
        ('cerrado', 'Cerrado')
    ], required=False)
    date = fields.Date(string="Fecha", required=False, )
    date_time = fields.Datetime(string="Fecha y hora", required=False, )



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