from odoo import models, fields


class CardpatientModel(models.Model):

    _name = 'cardpatient.model'
    _description = 'Card Patient'

    name = fields.Char()

    Doctor = fields.Many2many(
        comodel_name='doctor.model', )

    Diagnoz = fields.Many2many(
        comodel_name='diagnoz.model', )
