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


    titulo_id = fields.Many2one(comodel_name="titulo.odoo", string="Titulo", required=False, )
    campos_odoo_id = fields.One2many(comodel_name="campos.odoo.lines", inverse_name="campos_id", string="", required=False, )
    titulaciones = fields.Many2many(comodel_name="titulo.odoo", relation="campos_odoo_rel", column1="campos_id",
                                    column2="titulo_id", string="Titulaciones", )


class TitulosCampos(models.Model):
    _name = 'campos.odoo.lines'
    _description = 'líneas con las titulaciones del cliente'
    campos_id = fields.Many2one(comodel_name="campos.odoo", string="Líneas de títulos", required=False, )
    titulo_id = fields.Many2one(comodel_name="titulo.odoo", string="Título", required=False, )
    description = fields.Char(string="Description", required=False, )
