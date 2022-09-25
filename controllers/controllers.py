# -*- coding: utf-8 -*-
# from odoo import http


# class HospitalCustom(http.Controller):
#     @http.route('/hospital_custom/hospital_custom/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hospital_custom/hospital_custom/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('hospital_custom.listing', {
#             'root': '/hospital_custom/hospital_custom',
#             'objects': http.request.env['hospital_custom.hospital_custom'].search([]),
#         })

#     @http.route('/hospital_custom/hospital_custom/objects/<model("hospital_custom.hospital_custom"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hospital_custom.object', {
#             'object': obj
#         })
