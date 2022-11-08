from odoo import models, fields


class PatientCard(models.Model):
    _name = 'hospital.patient_card'  # назву моделі краще надавати за наступним форматом - загальна сутність, котру реалізує модуль ("hospital"), дочерня сутність ("patient") та піддочерню сутність ("card")
    _description = 'Patient Cards'

    name = fields.Char()

    doctor_ids = fields.Many2many(  # поля Many2many, One2many повинні мати суфікс "_ids" і бути написані з маленької літери
        comodel_name='hospital.doctor', )

    diagnoz_ids = fields.Many2many(  # поля Many2many, One2many повинні мати суфікс "_ids"
        comodel_name='hospital.diagnoz', )
