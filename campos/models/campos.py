# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Campos(models.Model):
    _name = 'campos.odoo'
    _description = 'Campos'

    name = fields.Char(string="Nombre", required=True ) #campo para el titulo del elemento
    active = fields.Boolean(string="Activo", help="Esta es la fila del campo" ) #campo con esto oculta el elemento en la lista
    description = fields.Text(string="Información del elemento", required=False )
    age = fields.Integer(string="Edad", required=True )
    title_id = fields.Many2one(comodel_name="titulos.odoo", string="Titulo" )
    titles_ids = fields.One2many(comodel_name="campos.odoo.lines", inverse_name="campos_id", string="Titulos" )
    titulaciones_ids = fields.Many2many(comodel_name="titulos.odoo", relation="campos_odoo_rel", column1="campos_id", column2="titulo_id", string="Titulaciones" )
    page_test = fields.Html(string="Crear página" )
    photo = fields.Binary(string="Fotografia" )
    state = fields.Selection(string="Color", selection=[('azul', 'Azul'), ('rojo', 'Rojo'), ], required=False )
    date = fields.Date(string="Fecha registro", required=False, )
    date_time = fields.Datetime(string="Fecha ultimo ingreso", required=False, )

class TitulosCampos(models.Model):
     _name = 'campos.odoo.lines'
     _description ='Lineas con titulos'

     campos_id = fields.Many2one(comodel_name="campos.odoo", string="Lineas de titulo" )
     titulo_id = fields.Many2one(comodel_name="titulos.odoo", string="Titulo")
     description = fields.Char(string="Descripción" )

#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100