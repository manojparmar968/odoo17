from odoo import models, fields, api, _

class OwlToDo(models.Model):
    _name  = 'owl.todo.list'
    _description = "Owl Todo List App"

    name = fields.Char("Task Name")
    completed = fields.Boolean()
    color = fields.Char()