from odoo import models, api, fields
class Tecnico (models.Model):
    _name = 'tecnico'
    _inherit=['mail.thread','mail.activity.mixin','portal.mixin']
    nombre = fields.Char(string="Nombre", required=False,)
    edad = fields.Char(string="Edad", required=False, )
    email = fields.Char(string="Email", required=False, )
    sexo = fields.Selection(string="Sexo", selection=[('hombre', 'Hombre'), ('mujer', 'Mujer'), ('otro', 'Otro'), ], required=False,)
    fecha_de_ingreso = fields.Date(string="Fecha de ingreso", required=False, )
    comentarios= fields.Text(string="Comentarios", required=False, )
    vehiculos_id= fields.Many2one(comodel_name="vehiculos.oodo", string="Vehiculo", required=False, )
    certificaciones_ids = fields.Many2many(comodel_name="certificacion.odoo", relation="tecnico_odoo_rel", column1="tecnico_id",column2="certificacion_id", string="Certificacion", ) #Por convencion debe terminar en _ids
    tecnico_id = fields.One2many(comodel_name="lineas_licencias.odoo", inverse_name="tecnicos_id", string="",
                                     required=False, )
    state = fields.Selection(string="Estado", selection=[('borrador', 'BORRADOR'), ('contratado', 'CONTRATADO'),
                                                         ('despedido', 'DESPEDIDO'), ('cancelado', 'CANCELADO')],
                             required=False, default='borrador')
    @api.multi
    def a_contratado(self):
        self.state = 'contratado'

    @api.multi
    def a_despedido(self):
        self.state= 'despedido'

    @api.multi
    def a_cancelado(self):
        self.state = 'cancelado'

class Lineas_licencias_tecnicos(models.Model):
    _name="lineas_licencias.odoo"
    _descripton="Lineas con las licencias de los tecnicos"
    tecnicos_id = fields.Many2one(comodel_name="tecnico", string="Tecnicos", required=False, ) #Por convencion debe terminar en _ids
    licencias_id = fields.Many2one(comodel_name="licencias.odoo", string="Licencias", required=False, )
    fecha_vencimiento = fields.Date(string="fecha vencimiento", required=False,)
