from odoo import models, fields, api, _

class Sale(models.Model):
    _inherit  = 'sale.order'

    def action_confirm(self):
        res = super(Sale,self).action_confirm()
        self.env['purchase.order'].create({
            'partner_id':self.partner_id.id,
            'origin' : self.name
        })
        return res