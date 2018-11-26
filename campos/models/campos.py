# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import datetime, timedelta, date

class Campos(models.Model):
    _name = 'campos.odoo'
    _description = 'Tabla praa registrar técnicos'
    _inherit =  ['mail.thread', 'mail.activity.mixin', 'portal.mixin']

    name = fields.Char(string="", required=False, track_visible='True' )
    active = fields.Boolean(string="Activo",default=True  )
    titulo_id = fields.Many2one(comodel_name="titulo.odoo", string="Titulo", required=False, )
    campos_odoo_ids = fields.One2many(comodel_name="campos.odoo.lines", inverse_name="campos_id", string="Lineas de titulos", required=False, )
    titulaciones_ids = fields.Many2many(comodel_name="titulo.odoo", relation="campos_odoo_rel", column1="campos_id", column2="titulo_id", string="Titulaciones", )
    otrarelacion_ids =  fields.Many2many(comodel_name="titulo.odoo", relation="campos_otrarelacion_rel", column1="campos_id", column2="otrarelacion_id", string="Otra Relacion", )
    otrarelacion2_ids = fields.Many2many(comodel_name="titulo.odoo", relation="campos_otrarelacion2_rel")
    vehiculos_id = fields.Many2one(comodel_name="vehiculos.odoo", string="Vehiculo", required=False, )
    licencias_ids = fields.One2many(comodel_name="licenciastecnico.odoo.lines", inverse_name="campos_id", string="Lineas de titulos", required=False, )
    certificaciones_ids = fields.Many2many(comodel_name="certificaciones.odoo", relation="campos_certificacion_rel", column1="tecnico_id", column2="certificaciones_id", string="Certificaciones", )
    state = fields.Selection(string="Estado", selection=[('borrador', 'BORRADOR'), ('contratado', 'CONTRATADO'), ('despedido', 'DESPEDIDO'),('cancelado', 'CANCELADO') ], required=False, default='borrador')
    time_onbusiness = fields.Char(string="Tiempo en la empresa",compute="_compute_time",  store=True)
    days_add = fields.Integer(string="Más días", required=False, )
    fecha_ingreso = fields.Date(string="Fecha de ingreso", required=False, )

    @api.depends('fecha_ingreso' )
    def _compute_amount(self):
        """
        @api.depends() should contain all fields that will be used in the calculations.
        """
        time= fields.Date.from.string(str(datetime.today())) - fields.Date.from.string(str((self.in_date) or datetime.today())[:10])
        self.fecha_ingreso = time + 0 #timedelta(days = self.days_add)

    @api.multi
    def a_contratado(self):
        self.state = 'contratado'

    @api.multi
    def a_despedido(self):
        self.state = 'despedido'

    @api.multi
    def a_cancelado(self):
        self.state = 'cancelado'

class TitulosCampos(models.Model):
    _name = 'campos.odoo.lines'
    _description= 'Lineas con las titulaciones del cliente'

    campos_id = fields.Many2one(comodel_name="campos.odoo", string="Lineas de titulos", required=False, )
    titulo_id = fields.Many2one(comodel_name="titulo.odoo", string="Titulo", required=False, )
    description = fields.Char(string="Descripcion", required=False, )


class LineasLicenciasTecnico(models.Model):
    _name = 'licenciastecnico.odoo.lines'
    _description= 'Lineas con las licencias del tecnico'

    campos_id = fields.Many2one(comodel_name="campos.odoo", string="Lineas de Campos", required=False, )
    licencia_id = fields.Many2one(comodel_name="licencias.odoo", string="Lineas de Licencias", required=False, )
    vencimiento_date = fields.Date(string="Fecha de vencimiento", required=False, )