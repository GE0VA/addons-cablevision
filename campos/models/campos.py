# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Campos(models.Model):
     _name = 'campos.odoo'

     name = fields.Char(string="Nombre", required=True, )
     active = fields.Boolean(string="Activo", help="Esta es la ayuda del campo" )
     decription = fields.Text(string="Descripción del registro", required=False, )
     html = fields.Html(string="Campo Html",  )
     amount = fields.Float(string="Monto",  required=False, )
     age = fields.Integer(string="Edad", required=False, )
     attachment = fields.Binary(string="Adjuntos",  )
     state = fields.Selection(string="Estado", selection=[
          ('borrador', 'Borrador'),
          ('validado', 'Validado'),
          ('close', 'Cerrado'),
     ], required=False, )
     date = fields.Date(string="Fecha registro", required=False, )
     date_time = fields.Datetime(string="Fecha y hora de registro", required=False, )






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