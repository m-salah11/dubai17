# -*- coding: utf-8 -*-
# from odoo import http


# class Projection(http.Controller):
#     @http.route('/projection/projection', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/projection/projection/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('projection.listing', {
#             'root': '/projection/projection',
#             'objects': http.request.env['projection.projection'].search([]),
#         })

#     @http.route('/projection/projection/objects/<model("projection.projection"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('projection.object', {
#             'object': obj
#         })

