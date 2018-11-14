# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Campos(models.Model):

    _name = 'campos.odoo'   #Se crea tabla en la base de datos se llama capos_odoo

    name = fields.Char(string="Nombre", required=True, )
    active = fields.Boolean(string="Activo", help="Esta es la ayuda del campo"  )
    descripcion = fields.Text(string="Descripcion del registro", required=False, )
    html= fields.Html(string="Campo Html",  )
    amount = fields.Float(string="Monto",  required=False, )
    age = fields.Integer(string="Edad", required=False, )
    attachment = fields.Binary(string="adjunto",  )
    state = fields.Selection(string="Estado", selection=[
        ('borrador', 'Borrador'),
        ('validado', 'Validado'),
        ('close', 'Cerrado')], required=False, )
    data= fields.Date(string="Fecha registro", required=False, )
    data_time= fields.Datetime(string="Fecha y hora del registro", required=False, )
    titulo_id= fields.Many2one(comodel_name="titulo.odoo", string="titulo", required=False, )
    campos_odoo_id= fields.One2many(comodel_name="campos.odoo.lines", inverse_name="campos_id", string="", required=False, )
    titulaciones = fields.Many2many(comodel_name="titulo.odoo",
                                    relation="titulo_odoo_rel",
                                    column1="campos_id",
                                    column2="titulo_id",
                                    string="Titulacion", )


    class TitulosCampos(models.Model):
        _name = 'campos.odoo.lines'
        _description ="lineas con los titulos del cliente"

        campos_id = fields.Many2one(comodel_name="campos.odoo", string="lineas de titulos", required=False, )
        titulo_id = fields.Many2one(comodel_name="titulo.odoo", string="titulo", required=False, )
        description= fields.Char(string="Descripcion", required=False, )
















    # class campos(models.Model):
#     _name = 'campos.campos'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100