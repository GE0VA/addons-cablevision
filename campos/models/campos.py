# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Campos(models.Model):
    _name = 'campos.odoo'   # se crea la tabla campos_odoo

    name = fields.Char(string="Nombre", required=True, )
    active = fields.Boolean(string="Activo", help="Esta es la ayuda del campo" )
    description = fields.Text(string="Descripción del registro", required=False, )
    html = fields.Html(string="Campo html",  )
    amount = fields.Float(string="Monto",  required=False, )
    age = fields.Integer(string="Edad", required=False, )
    attachment = fields.Binary(string="Adjuntos",  )
    state = fields.Selection(string="Estado", selection=[('borrador', 'Borrador'),
                                                         ('validado', 'Validado'),
                                                         ('close', 'Cerrado'),
                                                         ], required=False, )
    date = fields.Date(string="Fecha regisro", required=False, )
    datetime = fields.Datetime(string="Fecha y hora del registro", required=False, )

    titulo_id = fields.Many2one(comodel_name="titulo.odoo", string="Titulo", required=False, )


    campos_odoo_id = fields.One2many(comodel_name="campos.odoo.lines", inverse_name="campos_id", string="", required=False, )

    titulaciones_ids = fields.Many2many(comodel_name="titulo.odoo", relation="campos_odoo_rel", column1="campos_id", column2="titulo_id", string="Titulaciones", )

    class TitulosCampos(models.Model):
        _name = 'campos.odoo.lines'  # se crea la tabla campos_odoo
        description="Lineas con las titulaciones del cliente"
        campos_id = fields.Many2one(comodel_name="campos.odoo", string="Lineas de titulos", required=False, )
        titulo_id = fields.Many2one(comodel_name="titulo.odoo", string="Titulo", required=False, )
        description = fields.Char(string="Descripcion", required=False, )

