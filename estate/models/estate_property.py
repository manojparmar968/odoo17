from odoo import models, fields, api, _

class EstateProperty(models.Model):
    _name  = 'estate.property'
    _description = "Estate Property"

    name = fields.Char('Name', required=True, translate=True)
    description = fields.Text('Description')
    postcode = fields.Char('postcode')
    date_availability = fields.Date('Date Availability')
    expected_price = fields.Float('expected price', required=True)
    selling_price = fields.Float('selling price')
    bedrooms = fields.Integer('bedrooms')
    living_area = fields.Integer('living area')
    facades = fields.Integer('facades')
    garage = fields.Boolean('garage')
    garden = fields.Boolean('garden')
    garden_area = fields.Integer('garden area')
    garden_orientation = fields.Selection(string='garden orientation',
        selection=[
            ('north', 'North'), 
            ('south', 'South'),
            ('east', 'East'), 
            ('west', 'West')
        ],
    )