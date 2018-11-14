# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Tecnico(models.Model):
    _name = 'tecnico'
    _description = 'Tabla para registrar tecnicos'

    name = fields.Char(string='Nombre')
    age = fields.Char(string="Edad", required=False, )
    email = fields.Char(string="Email", required=False, )
    state = fields.Selection(string="Sexo",
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
        