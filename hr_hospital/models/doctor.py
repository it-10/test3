from odoo import models, fields


class Doctor(models.Model):
    _name = 'hospital.doctor'  # Слово "model" не потрібно додавати у назву
    _description = 'Doctors'

    name = fields.Char()
