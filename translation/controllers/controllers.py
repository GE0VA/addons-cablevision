# -*- coding: utf-8 -*-
from odoo import http

# class Translation(http.Controller):
#     @http.route('/translation/translation/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/translation/translation/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('translation.listing', {
#             'root': '/translation/translation',
#             'objects': http.request.env['translation.translation'].search([]),
#         })

#     @http.route('/translation/translation/objects/<model("translation.translation"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('translation.object', {
#             'object': obj
#         })