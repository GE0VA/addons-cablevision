# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Campos(models.Model):
    _name = 'campos.odoo'
    name = fields.Char(string="", required=False, )
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