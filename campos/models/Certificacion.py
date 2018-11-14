from odoo import models, api, fields
class Certificacion (models.Model):
    _name="certificacion.odoo"
    name = fields.Char(string="Nombre", required=False, )
    description= fields.Text(string="Descripcion", required=False, )
    fecha_curso = fields.Datetime(string="Fecha del curso", required=False, )