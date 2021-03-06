# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Campos(models.Model):
     _name = 'campos.odoo'
     # _inherit = ['mail.thread', 'mail.activity.mixin', 'portal.mixin']
     
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

     titulo_id = fields.Many2one(comodel_name="titulo.odoo", string="Titulo", required=False, )
     campos_odoo_ids = fields.One2many(comodel_name="campos.odoo.lines", inverse_name="campos_id", string="", required=False, )

     titulaciones_ids = fields.Many2many(comodel_name="titulo.odoo",
                                     relation="campos_odoo_rel",
                                     column1="campos_id",
                                     column2="titulo_id",
                                     string="Titulaciones", )
     
     # titulaciones = fields.Many2many(comodel_name="titulo.odoo", relation="titulo_odoo_rel", column1="campos_is", column2="titulo_id", string="Titulaciones", )
     # titulaciones2 = fields.Many2many(comodel_name="titulo.odoo",string="Titulaciones", )
     
class TitulosCampos(models.Model):
     _name = 'campos.odoo.lines'
     _description = "Lineas con las titulaciones del cliente"
     
     campos_id = fields.Many2one(comodel_name="campos.odoo", string="Lineas de titulos", required=False, )
     titulo_id = fields.Many2one(comodel_name="titulo.odoo", string="Titulo", required=False, )
     description = fields.Char(string="Descripcion", required=False, )
