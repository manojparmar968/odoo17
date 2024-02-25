from odoo import models, fields, api, _

class Sale(models.Model):
    _inherit  = 'sale.order'

    # @api.model_create_multi
    # def create(self, vals_list):
    #     super().create(vals_list)
    #     super()._create_invoices