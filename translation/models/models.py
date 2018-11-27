# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError


class Product(models.Model):
    _name = 'product'
    _description = 'Productos técnicos'

    name = fields.Char(string="Name", required=False, translate=True, copy=True)
    cost = fields.Float(string="Cost", required=False, translate=True, copy=True)
    sale_amount = fields.Float(string="Amount of sale", required=False, translate=True, copy=True)
    in_stock = fields.Float(string="In Stock", required=False, translate=True, copy=True)
    user_id = fields.Many2one(comodel_name="res.users", string="User", required=False, copy=True)
    categ = fields.Char(string="Category", required=False, translate=True)
    description = fields.Char(string="Short Description", required=False)
    long_description = fields.Html(string="Long descriptions", translate=True)

    @api.multi
    def write(self, values):
        return super(Product, self).writer(values)

