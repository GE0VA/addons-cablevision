# -*- coding: utf-8 -*-
from odoo import http

# class Campos(http.Controller):
#     @http.route('/campos/campos/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/campos/campos/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('campos.listing', {
#             'root': '/campos/campos',
#             'objects': http.request.env['campos.campos'].search([]),
#         })

#     @http.route('/campos/campos/objects/<model("campos.campos"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('campos.object', {
#             'object': obj
#         })