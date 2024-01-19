from odoo import api, fields, models, _
from odoo.exceptions import AccessError, MissingError, UserError, ValidationError

class ResPartner(models.Model):
    _inherit = "res.partner"

    def _create_menu_item_for_report(self):
        """ Adds a default menu item for this report. This is called by an action on the report, for reports created manually by the user.
        """
        self.ensure_one()

        action = self.env['ir.actions.client'].create({
            'name': self.name,
            'tag': 'res_partner',
            'context': {'report_id': self.id},
        })