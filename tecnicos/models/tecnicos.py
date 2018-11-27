# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import datetime, timedelta, date


class Tecnicos(models.Model):
    _name = 'tecnicos.odoo'
    _inherit = ['mail.thread', 'mail.activity.mixin', 'portal.mixin']

    name = fields.Char(string="Nombre y apellidos", required=True)
    age = fields.Char(string="Edad", size=2)
    email = fields.Char(string="Correo electrónico")
    genre = fields.Selection(string="Sexo", selection=[('M', 'Masculino'), ('F', 'Femenino'), ('O', 'Otro')])
    ingress_date = fields.Date(string="Fecha ingreso")
    comments = fields.Text(string="Comentarios")
    vehicule_id = fields.Many2one(comodel_name="vehiculos.odoo", string="Vehiculo")
    licenses_ids = fields.One2many(comodel_name="tecnicos.odoo.lines", inverse_name="tecnico_id", string="Licencias")
    titles_ids = fields.Many2many(comodel_name="titulos.odoo", relation="tecnico_odoo_rel", column1="tecnico_id",
                                  column2="titulo_id", string="Titulos")
    state = fields.Selection(string="Estado trabajador",
                             selection=[('0', 'Borrador'), ('1', 'Contratado'), ('2', 'Despedido'), ('3', 'Cancelado')],
                             track_visibility='always', default="0")
    labor_date = fields.Char(string="Tiempo laborado", compute="_compute_time", store=True)
    days_add = fields.Integer(string="Mas dias")

    licencia_id = fields.Many2one(comodel_name="licencias.odoo", string="Licencia", required=True)

    user_id = fields.Many2one(comodel_name='res.users', string='Usuario', required=False,
                              default=lambda self: self.env.user, copy=False)

    create_date = fields.Date(string='Fecha de creación', required=False, readonly=True,
                              default=fields.Date.context_today)

    send_welcome = fields.Boolean(string='Enviando email de bienvenida',
                                  default=False)

    score = fields.Char(string="Calificación",
                        required=False,
                        readonly=True,
                        compute='_compute_score')
    birth = fields.Date(string="Fecha de Nacimiento", required=True, )

    user = fields.Many2one(comodel_name="res.users",
                           string="Usuario que revisa",
                           required=False)
    date_revision = fields.Date(string="Fecha a revisar", required=False)

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
        # for license in self.licenses_ids:
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

    @api.model
    def _send_welcome_mail(self):
        print("1. Inicio enviío {hora}".format(hora=datetime.now()))
        tecnicos = self.search([('state', '=', '1'),
                                ('send_welcome', '=', False)])

        if not tecnicos:
            print("No hay tecnicos")
        for rec in tecnicos:
            values = {
                'author': 1,
                'body_html': ('<div>Hola %s!!! Bienvenido... </div>' % rec.name),
                'subject': 'Bienvenido %s' % rec.name,
                'email_from': 'odoo@andresgarita.com',
                'email_to': rec.email,
                'template_id': None
            }
            self.env['mail.mail'].create(values).send()
            rec.send_welcome = True
            print("Correo Enviado")


    @api.onchange('licencia_id')
    def onchange_licencia_id(self):
        self.vehicule_id = None


@api.depends('ingress_date', 'days_add')
def _compute_time(self):
    for rec in self:
        time = fields.Date.from_string(str(datetime.today())) - fields.Date.from_string(
            str(rec.ingress_date or datetime.today())[:10])
        rec.labor_date = time + timedelta(days=rec.days_add)  # self.days_add


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

    tecnico_id = fields.Many2one(comodel_name="tecnicos.odoo", string="Tecnicos")
    licencia_id = fields.Many2one(comodel_name="licencias.odoo", string="Licencias")
    fecha_vencimiento = fields.Date(string="Fecha de vencimiento")

#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100
