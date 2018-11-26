# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import datetime, timedelta, date

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
     licencia_tecnico = fields.Many2one( comodel_name="licencias.odoo", string="Licencia del vehiculo" )
     titles_ids = fields.Many2many( comodel_name="titulos.odoo", relation="tecnico_odoo_rel", column1="tecnico_id",
                                         column2="titulo_id", string="Titulos" )
     state = fields.Selection( string="Estado trabajador", selection=[('0', 'Borrador'), ('1', 'Contratado'), ('2', 'Despedido'), ('3', 'Cancelado')], track_visibility='always', default="0" )
     labor_date = fields.Char( string="Tiempo laborado", compute="_compute_time", store=True )
     days_add = fields.Integer( string="Mas dias" )
     date_create = fields.Date( string="Fecha de creacion", readonly=True, default=fields.Date.context_today )
     user_id = fields.Many2one( comodel_name="res.users", string="Usuario", default= lambda self: self.env.user, copy= False )
     score = fields.Char( string="Calificacion", readonly=True, compute="_compute_score" )
     birthday = fields.Date( string="", required=True )

     @api.depends('ingress_date', 'days_add') # la computacion depende de estos campos para ejecutarse
     def _compute_time(self):
          for rec in self:
              time = fields.Date.from_string(str(datetime.today())) - fields.Date.from_string(str((rec.ingress_date) or datetime.today())[:10])
              rec.labor_date = time + timedelta(days = rec.days_add)

     score = fields.Char(string="Calificación",
                         required=False,
                         readonly=True,
                         compute='_compute_score')
     birth = fields.Date(string="Fecha de Nacimiento", required=True, )

     @api.depends('ingress_date')
     def _compute_score(self):
          qualification = 0
          result = 'Malo'
          age = 0
          year, moth, day = [int(val) for val in (self.birth or '1990-12-01').split('-')]
          birth = date(year, moth, day)
          today = date.today()
          try:
               birthday = birth.replace(year=today.year)
          except:
               birthday = birthday.replace(year=today.year, day=birth.day - 1)

          if birthday > today:
               age = today.year - birth.year - 1
          else:
               age = today.year - birth.year

          # Si su edad es menor a 20, obtiene 2
          if age < 20:
               qualification = 2

          # si es mayor a 20 y menor a 40 obtiene 6
          if 20 <= age <= 40:
               qualification = 6

          # mayor de 40 obtiene 5
          if age > 40:
               qualification = 5

          # por cada licencia que tenga la persona se suman 2 puntos
          # for license in self.licencias_ids:
          #     qualification += 2

          qualification += len(self.licenses_ids) * 2

          # Si la puntuación es menor a 5 es Malo
          if qualification < 5:
               result = 'Malo'

          # de 5 a 8 Regular
          if 5 <= qualification <= 8:
               result = 'Regular'

          # mayor de 8 es Excelente
          if qualification > 8:
               result = 'Excelente'
          print("\n\nLos puntos de la calificacion son %s \n\n" % qualification)
          self.score = result

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