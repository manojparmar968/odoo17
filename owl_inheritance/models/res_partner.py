from odoo import api, fields, models, _
from odoo.exceptions import AccessError, MissingError, UserError, ValidationError

class ResPartner(models.Model):
    _inherit = "res.partner"

    username = fields.Char()
    expected_salary = fields.Integer()