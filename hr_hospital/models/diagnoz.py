from odoo import models, fields


class Diagnoz(models.Model):
    _name = 'hospital.diagnoz'
    _description = 'Diagnozes'

    name = fields.Char()
