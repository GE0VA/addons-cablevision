# -*- coding: utf-8 -*-


from odoo import models, fields, api
from datetime import datetime, timedelta, date

class tecnico(models.Model):

    _name = 'tecnico.odoo'
    _inherit = ['mail.thread', 'mail.activity.mixin','portal.mixin']


    name= fields.Char(string="Nombre", required=True, track_visibility='always' )
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

    # sesion 4 de la capacitacion

    time_onbusiness = fields.Char(string="Tiempo en la empresa", compute='_compute_time', store=True )

    days_add = fields.Integer(string="Mas dias", required=False, )

    licencias_id = fields.Many2one(comodel_name="licencias.odoo", string="Licencia", required=True, )

    date_create= fields.Date(string="Fecha de Creacion", required=False, readonly=True, default=fields.Date.context_today )
    user_id = fields.Many2one(comodel_name="res.users", string="Usuario", required=False, default =lambda self: self.env.user, copy= False )


    @api.depends('data', 'days_add')
    def _compute_time(self):



        for rec in self:

            time = fields.Date.from_string(str(datetime.today())) - fields.Date.from_string(str((rec.data) or datetime.today())[:10])
            rec.time_onbusiness = time + timedelta(days=rec.days_add)



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