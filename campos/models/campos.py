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


class TitulosCampos(models.Model):
    _name = 'campos.odoo.lines'
    _description= 'Lineas con las titulaciones del cliente'

    campos_id = fields.Many2one(comodel_name="campos.odoo", string="Lineas de titulos", required=False, )
    titulo_id = fields.Many2one(comodel_name="titulo.odoo", string="Titulo", required=False, )
    description = fields.Char(string="Descripcion", required=False, )