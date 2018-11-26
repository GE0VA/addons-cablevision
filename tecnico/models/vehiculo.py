# -*- coding: utf-8 -*-

from odoo import models, fields, api


class vehiculo(models.Model):
    _name = 'vehiculo.odoo'
    _descripcion = 'Almacenara los vehiculos relacionados con el tecnico'

    name = fields.Char(string="Nombre Vehiculo", required=True, )
    descrption = fields.Text(string="Descripcion Vehiculo", required=False, )
    placa = fields.Char(string="Placa", required=False, )

    #caṕacitacion sesion 4

    proper_license = fields.Many2one(comodel_name="licencias.odoo", string="Licencias para este Vehiculo", required=False, )
