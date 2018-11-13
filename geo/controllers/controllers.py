# -*- coding: utf-8 -*-
from odoo import http

# class Geo(http.Controller):
#     @http.route('/geo/geo/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/geo/geo/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('geo.listing', {
#             'root': '/geo/geo',
#             'objects': http.request.env['geo.geo'].search([]),
#         })

#     @http.route('/geo/geo/objects/<model("geo.geo"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('geo.object', {
#             'object': obj
#         })