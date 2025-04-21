# See LICENSE file for full copyright and licensing details.
from odoo import models, fields

class HrApplicant(models.Model):
    _inherit = 'hr.applicant'

    def _get_portal_url(self):
        self.ensure_one()
        return f"/my/job-applications/{self.id}"

    position_pdf = fields.Binary(string="Position Document")