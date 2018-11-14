# -*- coding: utf-8 -*-

from odoo import models, fields, api

from odoo import models, fields, api

class Tecnico(models.Model):
    _name = 'tecnico.odoo'  # se crea la tabla campos_odoo
    name = fields.Char(string="Nombre", required=True, )
    age = fields.Char(string="Edad", required=False, size=2, )
    email = fields.Char(string="Correo", required=False, )
    sexo = fields.Selection(string="Sexo", selection=[('mujer', 'Mujer'),
                                                      ('hombre', 'Hombre'),
                                                      ('otro', 'Otro'),
                                                      ], required=False, )
    date = fields.Date(string="Fecha de ingreso", required=False, )
    comments = fields.Text(string="Comentarios", required=False, )

    certificacion_id =fields.Many2many(comodel_name="certificacion.odoo", relation="tecnico_odoo_rel", column1="tecnico_id", column2="certificacion_id",
                                       string="Certificaciones", )

    licencia_odoo_id = fields.One2many(comodel_name="tecnico.odoo.lines", inverse_name="tecnico_id", string="",  required=False, )

    vehiculo_id = fields.Many2one(comodel_name="vehiculo.odoo", string="Vehiculo", required=False, )
    state = fields.Selection(string="Estado", selection=[
        ('borrador', 'BORRADOR'),
        ('contratado', 'CONTRATADO'),
        ('despedido', 'DESPEDIDO'),
        ('cancelado', 'CANCELADO'),

    ], required=False, default='borrador')

    @api.multi
    def a_contratado(self):
        self.sate='contratado'

    @api.multi
    def a_despedido(self):
        self.sate = 'despedido'

     @api.multi
     def a_cancelado(self):
        self.sate = 'cancelado'

class LicenciaTecnico(models.Model):
    _name = 'tecnico.odoo.lines'  # se crea la tabla campos_odoo
    description="Lineas con las licencias del tecnico"

    tecnico_id = fields.Many2one(comodel_name="tecnico.odoo", string="Lineas de tecnico", required=False, )
    licencia_id = fields.Many2one(comodel_name="licencia.odoo", string="Licencias", required=False, )
    date = fields.Datetime(string="Fecha vencimiento ", required=False, )

# class tecnico(models.Model):
#     _name = 'tecnico.tecnico'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100