# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError

class Product(models.Model):
    _name = 'product'
    _description = 'Productos tecnico'

    name = fields.Char(string="Name", required=False, translate=True,copy=True)
    cost = fields.Float(string="Cost",  required=False, translate=True,copy=True)
    sale_amount = fields.Float(string="Amount of Sale",  required=False, copy=True, translate=True)
    in_stock = fields.Float(string="In stock",  required=False, translate=True, copy=True)
    user_id = fields.Many2one(comodel_name="res.users",
                              string="User",
                              required=False,
                              copy=False)
    categ = fields.Char(string="Category", required=False, translate=True)
    description = fields.Char(string="Short Description", required=False, )
    long_description = fields.Html(string="Long Description", translate=True)
    
    @api.multi
    def write(self, values):
        # raise UserError(_('This text is not translated.'))
        return super(Product, self).write(values)