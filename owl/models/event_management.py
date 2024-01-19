from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

class EventManagement(models.Model):
    _name = 'event.management'
    _description = "event management"

    name = fields.Char('Name', required=True)
    start_date = fields.Date('start date')
    end_date = fields.Date('end date')
    seats = fields.Integer('seats')
    location = fields.Char('location')
    state = fields.Selection(string='state',
        selection=[
            ('draft', 'Draft'), 
            ('confirmed', 'Confirmed'),
            ('done', 'Done')
        ], default='draft',
    )

    def action_confirm(self):
        if self.state == 'draft':
            self.state = 'confirmed'
    
    @api.constrains('start_date', 'end_date')
    def _check_dates(self):
        for record in self:
            if record.start_date and record.end_date and record.start_date > record.end_date:
                raise ValidationError("End date must be greater than or equal to start date.")
        