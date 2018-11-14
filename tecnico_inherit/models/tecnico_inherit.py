from odoo import api,models, fields

class InheritTecnico(models.Model):
    _inherit='campos.odoo'

    calle1 = fields.Char(string="Calle1", required=False, )
    ciudad = fields.Char(string="Ciudad", required=False, )
    pais = fields.Many2one(comodel_name="res.country", string="Pais", required=False, )
    provincia = fields.Many2one(comodel_name="res.country.state", string="Estado", required=False, )
    active = fields.Boolean(string="Activo", )