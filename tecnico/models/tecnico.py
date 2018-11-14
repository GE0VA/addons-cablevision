# -*- coding: utf-8 -*-

from odoo import models, fields, api

class tecnico(models.Model):

    _name = 'tecnico.odoo'

    name= fields.Char(string="Nombre", required=True, )
    age= fields.Char(string="Edad", required=False, size=2,  )
    email = fields.Char(string="Correo", required=False, )
    sexo = fields.Selection(string="Genero", selection=[('Hombre', 'Masculino'), ('Mujer', 'Femenino'), ('otro', 'Otro') ], required=False, )
    data = fields.Date(string="Fecha Ingreso", required=False, )
    Comen = fields.Text(string="Comentario", required=False, )
    vehiculo_id = fields.Many2one(comodel_name="vehiculo.odoo", string="Vehiculo", required=False, )
    licencias_ids = fields.One2many(comodel_name="tecnico.odoo.licencia.line", inverse_name="licencia_id", string="Licencias", required=False, )
    certificaciones_ids = fields.Many2many(comodel_name="certificacion.odoo", relation="tecnico_certificacion_rel", column1="tecnico_id", column2="certificacion_id", string="Certificaciones", )
    state = fields.Selection(string="Estado",
                             selection=[('borrador', 'Borrador'),
                                        ('contratado', 'Contratado'),
                                        ('despedido', 'Despedido'),
                                        ('cancelado', 'Cancelado') ], required=False, default='borrador' )


    @api.multi
    def a_contratado(self):
        self.state='contratado'

    @api.multi
    def a_despedido(self):
        self.state = 'despedido'

    @api.multi
    def a_cancelado(self):
        self.state = 'cancelado'

class LineasLicenciaTecnico(models.Model):
    _name = 'tecnico.odoo.licencia.line'
    _description ="lineas con los titulos del cliente"

    tecnico_id = fields.Many2one(comodel_name="tecnico.odoo", string="lineas de tecnico", required=False, )
    licencia_id = fields.Many2one(comodel_name="licencias.odoo", string="Licencia", required=False, )
    fecha_vencimineto = fields.Date(string="Fecha de vencimineto", required=False, )







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