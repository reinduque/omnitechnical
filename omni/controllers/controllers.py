# -*- coding: utf-8 -*-
# from odoo import http


# class Omni(http.Controller):
#     @http.route('/omni/omni/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/omni/omni/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('omni.listing', {
#             'root': '/omni/omni',
#             'objects': http.request.env['omni.omni'].search([]),
#         })

#     @http.route('/omni/omni/objects/<model("omni.omni"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('omni.object', {
#             'object': obj
#         })
