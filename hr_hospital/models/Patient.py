import logging

from odoo import models, fields

_logger = logging.getLogger(__name__)


class PatientModel(models.Model):
    _name = 'patient.model'
    _description = 'Patient'

    name = fields.Char()

    CardPatient = fields.Many2many(
        comodel_name='cardpatient.model', )
