from odoo import models, fields, _, api

class InheritSaleOrder(models.Model):
    _inherit = "sale.order"

    sale_description = fields.Char(string='Sale Description')