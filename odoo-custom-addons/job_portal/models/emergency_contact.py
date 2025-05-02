# See LICENSE file for full copyright and licensing details.
from odoo import fields, models, _


class EmergencyContact(models.Model):
    _name = 'emergency.contact'
    _description = 'Emergeny Contact'

    name = fields.Char()
    relation = fields.Char('Relationship')
    phone = fields.Char('Phone')
    employee_id = fields.Many2one('hr.employee', string='Employee')
    applicant_id = fields.Many2one('hr.applicant', string='Application')
    partner_id = fields.Many2one('res.partner', string='Partner')
