# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Tecnicos(models.Model):
     _name = 'tecnicos.odoo'
     _inherit = ['mail.thread', 'mail.activity.mixin', 'portal.mixin']

     name = fields.Char( string="Nombre y apellidos", required=True )
     age = fields.Char( string="Edad", size=2 )
     email = fields.Char( string="Correo electrónico" )
     genre = fields.Selection( string="Sexo", selection=[('H', 'Hombre'), ('M', 'Mujer'), ('O', 'Otro')] )
     ingress_date = fields.Date( string="Fecha ingreso" )
     comments = fields.Text( string="Comentarios" )
     vehicule_id = fields.Many2one( comodel_name="vehiculos.odoo", string="Vehiculo" )
     licenses_ids = fields.One2many( comodel_name="tecnicos.odoo.lines", inverse_name="tecnico_id", string="Licencias" )
     titles_ids = fields.Many2many( comodel_name="titulos.odoo", relation="tecnico_odoo_rel", column1="tecnico_id",
                                         column2="titulo_id", string="Titulos" )
     state = fields.Selection(string="Estado trabajador", selection=[('0', 'Borrador'), ('1', 'Contratado'), ('2', 'Despedido'), ('3', 'Cancelado')], track_visibility='always', default="0" )

     @api.multi
     def a_contratado(self):
         self.state = '1'

     @api.multi
     def a_despedido(self):
         self.state = '2'

     @api.multi
     def a_cancelado(self):
         self.state = '3'

class TecnicosLicencias(models.Model):
     _name = 'tecnicos.odoo.lines'

     tecnico_id = fields.Many2one( comodel_name="tecnicos.odoo", string="Tecnicos" )
     licencia_id = fields.Many2one( comodel_name="licencias.odoo", string="Licencias" )
     fecha_vencimiento = fields.Date( string="Fecha de vencimiento" )

#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100