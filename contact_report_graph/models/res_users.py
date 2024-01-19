from odoo import api, models, modules
from odoo.exceptions import AccessError, MissingError, UserError, ValidationError

class Users(models.Model):
    _inherit = 'res.users'
