# -*- coding: utf-8 -*-
# from odoo import http


# class EtlLauncher(http.Controller):
#     @http.route('/etl_launcher/etl_launcher/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/etl_launcher/etl_launcher/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('etl_launcher.listing', {
#             'root': '/etl_launcher/etl_launcher',
#             'objects': http.request.env['etl_launcher.etl_launcher'].search([]),
#         })

#     @http.route('/etl_launcher/etl_launcher/objects/<model("etl_launcher.etl_launcher"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('etl_launcher.object', {
#             'object': obj
#         })
