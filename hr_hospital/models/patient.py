import logging

from odoo import models, fields

_logger = logging.getLogger(__name__)


class Patient(models.Model):
    _name = 'hospital.patient'
    _description = 'Patients'

    name = fields.Char()

    card_ids = fields.Many2many(
        comodel_name='hospital.patient_card', )
