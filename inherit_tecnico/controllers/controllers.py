# -*- coding: utf-8 -*-
from odoo import http

# class InheritTecnico(http.Controller):
#     @http.route('/inherit_tecnico/inherit_tecnico/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/inherit_tecnico/inherit_tecnico/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('inherit_tecnico.listing', {
#             'root': '/inherit_tecnico/inherit_tecnico',
#             'objects': http.request.env['inherit_tecnico.inherit_tecnico'].search([]),
#         })

#     @http.route('/inherit_tecnico/inherit_tecnico/objects/<model("inherit_tecnico.inherit_tecnico"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('inherit_tecnico.object', {
#             'object': obj
#         })