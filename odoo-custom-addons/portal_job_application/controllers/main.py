from odoo import http
from odoo.http import request
from odoo.addons.portal.controllers.portal import CustomerPortal
import base64

class PortalJobApplication(CustomerPortal):

    def _prepare_home_portal_values(self, counters):
        values = super()._prepare_home_portal_values(counters)
        if 'job_app_count' in counters:
            count = request.env['hr.applicant'].sudo().search_count([('partner_id', '=', request.env.user.partner_id.id)])
            values['job_app_count'] = count
        return values

    @http.route(['/my/job-applications'], type='http', auth="user", website=True)
    def portal_my_applications(self, **kwargs):
        applicants = request.env['hr.applicant'].sudo().search([
            ('partner_id', '=', request.env.user.partner_id.id)
        ])
        return request.render('portal_job_application.portal_my_applications', {
            'applicants': applicants
        })


    @http.route(['/my/job-applications/upload'], type='http', auth="user", methods=['POST'], csrf=True, website=True)
    def upload_position_document(self, **post):
        applicant_id = post.get('applicant_id')
        upload_file = post.get('position_pdf')  # This should match your input's name in the HTML form

        if applicant_id and upload_file:
            try:
                applicant_id = int(applicant_id)
                applicant = request.env['hr.applicant'].sudo().browse(applicant_id)

                if applicant.exists():
                    # Read file and save into Binary field
                    file_data = base64.b64encode(upload_file.read())
                    applicant.write({
                        'position_pdf': file_data
                    })
                    # Optional: Post message in chatter
                    applicant.message_post(body="📎 New position document uploaded by applicant via portal.")

            except Exception as e:
                # Log or handle any error if needed
                return request.redirect('/my/job-applications?error=1')

        return request.redirect('/my/job-applications')