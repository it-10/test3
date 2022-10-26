from odoo import models, fields


class DiagnozModel(models.Model):
    _name = 'diagnoz.model'
    _description = 'Diagnoz'

    name = fields.Char()
