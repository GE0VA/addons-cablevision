# -*- coding: utf-8 -*-

from odoo import models, fields, api


class certificacion(models.Model):
    _name = 'certificacion.odoo'
    _descripcion = 'Almacenara los vehiculos relacionados con el tecnico'

    name= fields.Char(string="Nombre Certificacion", required=True, )
    descrption_certificacion = fields.Text(string="Descripcion certificacion", required=False, )
    fecha_curso = fields.Datetime(string="Fecha del curso", required=False, )