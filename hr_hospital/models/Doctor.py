from odoo import models, fields


class DoctorModel(models.Model):
    _name = 'doctor.model'
    _description = 'Doctor'

    name = fields.Char()
