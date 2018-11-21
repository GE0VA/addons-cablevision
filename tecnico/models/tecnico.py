# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import datetime, timedelta
from datetime import date

class Tecnico(models.Model):
    _name = 'tecnico'
    _description = 'Tabla para registrar tecnicos'
    _inherit = ['mail.thread', 'mail.activity.mixin', 'portal.mixin']

    name = fields.Char(string='Nombre',track_visibility='always')
    age = fields.Char(string="Edad", required=False, )
    email = fields.Char(string="Email", required=False, )
    sexo = fields.Selection(string="Sexo",
                             selection=[
                                 ('m', 'Masculino'),
                                 ('f', 'Femenino'),
                             ],
                             required=False, )
    in_date = fields.Date(string="Fecha de Ingreso", required=False, )
    comment = fields.Text(string="Comentarios", required=False, )
    vehicle_id = fields.Many2one(comodel_name="vehicle", string="Vehiculo", required=False, )
    licencias_ids = fields.One2many(comodel_name="tecnico.licencias.line", inverse_name="tecnico_id", string="Licencias", required=False, )
    certificciones_ids = fields.Many2many(comodel_name="certificaciones", relation="tecnico_certificaciones_rel", column1="tecnico_id", column2="certificacion_id", string="", )
    state = fields.Selection(string="Estado",
                             selection=[
                                 ('borrador', 'BORRADOR'),
                                 ('contratado', 'CONTRATADO'),
                                 ('despedido', 'DESPEDIDO'),
                                 ('cancelado', 'CANCELADO'),
                             ], required=False, default='borrador' )

    # 4 -PARTE---------------------------------------------------------------------------------------------------------
    date_create = fields.Date(string="Fecha de Creación", required=False,readonly=True, default=fields.Date.context_today )

    # 4 -PARTE---------------------------------------------------------------------------------------------------------

    # 3 -PARTE---------------------------------------------------------------------------------------------------------
    licencia_id = fields.Many2one(comodel_name="licencias", string="Licencia", required=True, )

    # 3 -PARTE---------------------------------------------------------------------------------------------------------
    
    
    # 1 -PARTE---------------------------------------------------------------------------------------------------------
    time_onbusiness = fields.Char(string="Tiempo en la Empresa", required=False, compute="_compute_time", store=True )
    days_add = fields.Integer(string="Mas dias", required=False, )
    
    @api.depends('in_date','days_add')
    def _compute_time(self):
        """
        api.depends Este decorador hace que cuando se modifique algun campo agregado al api.depends se ejecute el metodo
        Si lo ponemos en un campo calculado con atributo store=True entonces hara que el metodo se ejecute cuando esos campos sean modificados

        :return:
        """
        # time = fields.Date.from_string(str(datetime.today())) - fields.Date.from_string(str(self.in_date))
        time = fields.Date.from_string(str(datetime.today())) - fields.Date.from_string(str((self.in_date) or datetime.today())[:10]) #TODO PUNTO 4
        self.time_onbusiness = time + timedelta(days=self.days_add)
    # 1 -PARTE---------------------------------------------------------------------------------------------------------

    # 5 -PARTE---------------------------------------------------------------------------------------------------------
    score = fields.Char(string="Calificación", required=False,readonly=True, compute='_compute_score' )
    birth = fields.Date(string="Fecha de Nacimiento", required=True, )

    @api.depends('in_date')
    def _compute_score(self):
        age = 0
        year, moth, day = [int(val) for val in (self.birth or '1990-12-01').split('-') ]
        birth = date(year, moth, day)
        today = date.today()
        try:
            birthday = birth.replace(year=today.year)
        except:
            birthday = birthday.replace(year=today.year,day=birth.day - 1)
        
        if birthday > today:
            age = today.year - birth.year - 1
        else:
            age = today.year - birth.year
        
        self.score = age

    # 5 -PARTE---------------------------------------------------------------------------------------------------------

    
    
    @api.multi
    def a_contratado(self):
        self.state = 'contratado'
        
    @api.multi
    def a_despedido(self):
        self.state = 'despedido'
        
    @api.multi
    def a_cancelado(self):
        self.state = 'cancelado'
        
    
    # value2 = fields.Float(compute="_value_pc", store=True)
    #
    # @api.depends('value')
    # def _value_pc(self):
    #     self.value2 = float(self.value) / 100

    class TecnicoLicenciasLine(models.Model):
        _name = 'tecnico.licencias.line'
        _description = 'Licencias de para tecnicos'

        tecnico_id = fields.Many2one(comodel_name="tecnico", string="Lineas de Licencias", required=False, )
        licencia_id = fields.Many2one(comodel_name="licencias", string="Licencia", required=False, )
        date_due = fields.Date(string="Fecha de Vencimiento", required=False, )
        