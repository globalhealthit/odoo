import base64
from datetime import datetime
import logging
import odoo.addons.website_sale.controllers.main
from odoo import SUPERUSER_ID, http, _
from odoo.addons.portal.controllers.portal \
    import CustomerPortal as CustomerPortal, pager as portal_pager
from odoo.addons.website_hr_recruitment.controllers.main import WebsiteHrRecruitment as Home
from odoo.http import request
import json
_logger = logging.getLogger(__name__)


class CustomController(http.Controller):

    @http.route(['/page/get_state_applicant'], type='json', auth="public")
    def get_state_applicant(self, country_id):
        states = request.env['res.country.state'].search(
            [('country_id.id', '=', country_id)])
        list = []
        for state in states:
            list.append({'id': state.id, 'name': state.name})
        return list

    @http.route(['/add_academic_applicant'], type='json', auth="public", website=True)
    def add_academic_applicant(self, **kwargs):
        """A Method used to add Academic details of the applicant.

        Returns:
            It returns True after creating the record for
            the education of the applicant.
        """
        vals = {
            'organization': kwargs.get('organization'),
            'location': kwargs.get('location'),
            'name': kwargs.get('qualification'),
            'study_field': kwargs.get('study_field'),
            'start_date': kwargs.get('start_date'),
            'grade': kwargs.get('grade'),
            'partner_id': request.env['res.users'].browse(
                request.uid).partner_id.id,
        }
        if kwargs.get('end_date'):
            vals.update({'end_date': kwargs.get('end_date')})
        if kwargs.get('is_still'):
            vals.update({'is_still': True})
        else:
            vals.update({'is_still': False})
        return request.env['hr.academic'].sudo().create(vals).id

    @http.route(['/edit_academic_applicant'], type='json', auth="public", website=True)
    def edit_academic_applicant(self, **kwargs):
        """A Method used to Edit Academic details of the applicant.

        Returns:
            It returns True after updating the record for
            the education of the applicant.
        """
        vals = {
            'organization': kwargs.get('organization'),
            'location': kwargs.get('location'),
            'name': kwargs.get('qualification'),
            'study_field': kwargs.get('study_field'),
            'start_date': kwargs.get('start_date'),
            'grade': kwargs.get('grade'),
            'partner_id': request.env['res.users'].browse(
                request.uid).partner_id.id,
        }
        if kwargs.get('end_date'):
            vals.update({'end_date': kwargs.get('end_date')})
        if kwargs.get('is_still'):
            vals.update({'is_still': True})
            vals.update({'end_date': None})
        else:
            vals.update({'is_still': False})
        request.env['hr.academic'].sudo().browse(
            int(kwargs.get('id'))).write(vals)
        return kwargs.get('id')

    @http.route(['/delete_academic'], type='json', auth="public",
                website=True)
    def delete_academic(self, **kwargs):
        """A Method used to Delete Academic detail of the applicant.

        Returns:
            It returns True after creating the record for
            the education of the applicant.
        """
        return request.env['hr.academic'].sudo().browse(
            kwargs.get('id')).unlink()

    @http.route(['/add_experience'], type='json', auth="public",
                website=True)
    def add_experience(self, **kwargs):
        """A Method used to add Experience Details of the applicant.

        Returns:
            It returns True after creating the record for
            the Experience Details of the applicant.
        """

        vals = {
            'name': kwargs.get('job_position'),
            'description': kwargs.get('description'),
            'organization': kwargs.get('organization'),
            'location': kwargs.get('location'),
            'start_date': kwargs.get('start_date'),
            'partner_id': request.env['res.users'].browse(
                request.uid).partner_id.id,
            'type': kwargs.get('type'),
        }
        if kwargs.get('end_date'):
            vals.update({'end_date': kwargs.get(
                'end_date'), 'is_still': False})
        if kwargs.get('is_still'):
            vals.update({'end_date': None, 'is_still': True})
        else:
            vals.update({'is_still': False})
        return request.env['hr.experience'].sudo().create(vals).id

    @http.route(['/edit_experience_applicant'], type='json', auth="public",
                website=True)
    def edit_experience_applicant(self, **kwargs):
        """A Method used to Edit Experience details of the applicant.

        Returns:
            It returns True after updating the record for
            the Experience of the applicant.
        """

        vals = {
            'name': kwargs.get('job_position'),
            'description': kwargs.get('description'),
            'organization': kwargs.get('organization'),
            'location': kwargs.get('location'),
            'start_date': kwargs.get('start_date'),
            'partner_id': request.env['res.users'].browse(
                request.uid).partner_id.id,
            'type': kwargs.get('type'),
        }
        if kwargs.get('end_date') and not kwargs.get('is_still'):
            vals.update({'end_date': kwargs.get('end_date')})
        if kwargs.get('is_still'):
            vals.update({'end_date': None, 'is_still': True})
        else:
            vals.update({'is_still': False})
        request.env['hr.experience'].sudo().browse(
            int(kwargs.get('id'))).write(vals)
        return int(kwargs.get('id'))

    @http.route(['/delete_experience'], type='json', auth="public",
                website=True)
    def delete_experience(self, **kwargs):
        """A Method used to Delete Experience of the applicant.

        Returns:
            It returns True after creating the record for
            the education of the applicant.
        """
        return request.env['hr.experience'].sudo().browse(
            kwargs.get('id')).unlink()

    @http.route(['/add_certification'], type='json', auth="public",
                website=True)
    def add_certification(self, **kwargs):
        """A Method used to add Certiifcation details of the applicant.

        Returns:
            It returns True after creating the record for
            the Certiifcation of the applicant.
        """

        vals = {
            'certification': kwargs.get('certification'),
            'name': kwargs.get('name'),
            'description': kwargs.get('description'),
            'organization': kwargs.get('organization'),
            'location': kwargs.get('location'),
            'start_date': kwargs.get('start_date'),
            'grade': kwargs.get('grade'),
            'partner_id': request.env['res.users'].browse(
                request.uid).partner_id.id,
        }
        if kwargs.get('end_date'):
            vals.update({'end_date': kwargs.get('end_date')})
        if kwargs.get('is_still'):
            vals.update({'is_still': True, 'end_date': None})
        else:
            vals.update({'is_still': False})
        return request.env['hr.certification'].sudo().create(vals).id

    @http.route(['/edit_certification_applicant'], type='json', auth="public",
                website=True)
    def edit_certification_applicant(self, **kwargs):
        """A Method used to Edit Certification details of the applicant.

        Returns:
            It returns True after updating the record for
            the Certification of the applicant.
        """
        vals = {
            'certification': kwargs.get('certification'),
            'name': kwargs.get('name'),
            'description': kwargs.get('description'),
            'organization': kwargs.get('organization'),
            'location': kwargs.get('location'),
            'start_date': kwargs.get('start_date'),
            'grade': kwargs.get('grade'),
            'partner_id': request.env['res.users'].browse(
                request.uid).partner_id.id,
        }
        if kwargs.get('end_date'):
            vals.update({'end_date': kwargs.get('end_date')})
        if kwargs.get('is_still'):
            vals.update({'is_still': True})
            vals.update({'end_date': None})
        else:
            vals.update({'is_still': False})
        request.env['hr.certification'].sudo().browse(
            int(kwargs.get('id'))).write(vals)
        return int(kwargs.get('id'))

    @http.route(['/delete_certificate'], type='json', auth="public",
                website=True)
    def delete_certificate(self, **kwargs):
        """A Method used to Delete Certification detail of the applicant.

        Returns:
            It returns True after creating the record for
            the education of the applicant.
        """
        return request.env['hr.certification'].sudo().browse(
            kwargs.get('id')).unlink()
        
        
    @http.route(['/add_emergency_contact'], type='json', auth="public", website=True)
    def add_emergency_contact(self, **kwargs):
        """A Method used to add Emergency Contact details of the applicant.

        Returns:
            It returns True after creating the record for
            the emergency contact of the applicant.
        """
        vals = {
            'name': kwargs.get('name'),
            'relation': kwargs.get('relation'),
            'phone': kwargs.get('phone'),
            'partner_id': request.env['res.users'].browse(request.uid).partner_id.id,
        }
        return request.env['emergency.contact'].sudo().create(vals).id

    @http.route(['/edit_emergency_contact'], type='json', auth="public", website=True)
    def edit_emergency_contact(self, **kwargs):
        """A Method used to Edit Emergency Contact details of the applicant.

        Returns:
            It returns True after updating the record for
            the emergency contact of the applicant.
        """
        vals = {
            'name': kwargs.get('name'),
            'relation': kwargs.get('relation'),
            'phone': kwargs.get('phone'),
            'partner_id': request.env['res.users'].browse(request.uid).partner_id.id,
        }
        request.env['emergency.contact'].sudo().browse(
            int(kwargs.get('id'))).write(vals)
        return kwargs.get('id')

    @http.route(['/delete_emergency_contact'], type='json', auth="public",
                website=True)
    def delete_emergency_contact(self, **kwargs):
        """A Method used to Delete Emergency Contact detail of the applicant.

        Returns:
            It returns True after creating the record for
            the education of the applicant.
        """
        return request.env['emergency.contact'].sudo().browse(
            kwargs.get('id')).unlink()


class InheritedCustomerPortal(CustomerPortal):
    """Updated the Optional fields list to stop the unkown fields error."""
    MANDATORY_BILLING_FIELDS = [
        "name", "email", "street", "city", "country_id"]
    OPTIONAL_BILLING_FIELDS = ["zipcode", "state_id", "phone", "vat", "mobile", "company_name",
                               "organization", "location", "study_field",
                               "grade", "job_position", "start_date", "description",
                               "end_date", "qualification", "certification",
                               "operation_type", "opr_id", "tr_no",
                               "is_still"]

    def _prepare_portal_layout_values(self):
        values = super(InheritedCustomerPortal,
                       self)._prepare_portal_layout_values()
        partner = request.env.user.partner_id
        applicant_obj = request.env['hr.applicant']
        application_count = applicant_obj.sudo().search_count(
            [('email_from', '=', partner.email)])
        values.update({
            'application_count': application_count,
        })
        return values

    @http.route(['/my/applications', '/my/applications/page/<int:page>'],
                type='http', auth="user", website=True)
    def portal_my_applicantions(self, page=1, sortby=None, **kw):
        values = self._prepare_portal_layout_values()
        partner = request.env.user.partner_id
        applicant_obj = request.env['hr.applicant']
        domain = [('email_from', '=', partner.email)]
        searchbar_sortings = {
            'job': {'label': _('Applied Job'), 'order': 'job_id'},
            'department': {'label': _('Department'), 'order': 'department_id'},
        }

        if not sortby:
            sortby = 'job'
        sort_order = searchbar_sortings[sortby]['order']

        application_count = applicant_obj.search_count(domain)
        pager = portal_pager(
            url="/my/applications",
            url_args={'sortby': sortby},
            total=application_count,
            page=page,
            step=self._items_per_page
        )
        applications = applicant_obj.search(domain, order=sort_order,
                                            limit=self._items_per_page,
                                            offset=pager['offset'])
        request.session['my_leads_history'] = applications.ids[:100]

        values.update({
            'applications': applications.sudo(),
            'pager': pager,
            'page_name': 'Applications',
            'default_url': '/my/applications',
            'searchbar_sortings': searchbar_sortings,
            'sortby': sortby,
        })
        return request.render("job_portal.portal_my_application", values)

    @http.route(['/my/applications/<int:application_id>'], type='http',
                auth="user", website=True)
    def portal_application_page(self, application_id, **kw):
        application = request.env['hr.applicant'].sudo().search(
            [('id', '=', application_id)])
        values = {
            'partner_id': request.env.user.partner_id.id,
            'application': application,
            'page_name': 'Applications',
        }
        return request.render('job_portal.portal_job_application', values)


class WebsiteHrRecruitment(Home):
    """This class is defined to enhance HR Recruitment portal."""

    @http.route('''/jobs/apply/<model("hr.job"):job>''', type='http', auth="user", website=True, sitemap=True)
    def jobs_apply(self, job, **kwargs):
        """A Method for the users to be able to apply for job.
        Args:
            job: The first parameter to fetch the job position.
            kwargs: The second parameter to get the details of
            the job applicant.
        Returns:
            It renders the template & creates a record for job
            application.
        """
        error = {}
        default = {}
        env = request.env(context=dict(request.env.context, show_address=True, no_tag_br=True))
        applicant_1 = request.env['hr.applicant'] \
            .search([('partner_id', '=', request.env.user.partner_id.id)],
                    limit=1, order='create_date desc')
        countries = env['res.country'].sudo().search([])
        states = env['res.country.state'].sudo().search([])

        if 'website_hr_recruitment_error' in request.session:
            error = request.session.pop('website_hr_recruitment_error')
            default = request.session.pop('website_hr_recruitment_default')
        return request.render("job_portal.apply", {
            'applicant': applicant_1,
            'job': job,
            'error': error,
            'default': default,
            'countries': countries,
            'states': states,
            'partner': request.env['res.users'].sudo().browse(
                request.uid).partner_id,
        })

    def _get_applicant_char_fields(self):
        """A Helper Method to get the applicants's Char fields."""
        return ['gender',
                'marital', 'partner_mobile', 'email_from',
                'street_ht', 'street2_ht', 'city_ht', 'zip_ht',
                ]

    def _get_applicant_relational_fields(self):
        """A Helper Method to get the applicants's Relational fields."""
        return ['department_id', 'job_id', 'country_id', 'state_id_ht']

    def _get_applicant_files_fields(self):
        """A Helper Method to get the applicants's File fields."""
        return ['ufile']

    def _get_residential_address(self, kwargs):
        """A Helper Method to get the applicants's residential address."""
        address = {
            'name': kwargs.get('name'),
            'street': kwargs.get('street'),
            'street2': kwargs.get('street2') or '',
            'city': kwargs.get('city'),
            'zip': kwargs.get('zip'),
            'state_id': kwargs.get('state_id'),
            'country_id': kwargs.get('country_id'),
            'mobile': kwargs.get('partner_mobile'),
            'email': kwargs.get('email_from'),
            'customer': False,
        }
        return address

    def _format_date(self, date):
        """A Helper Method to get the formated value of the date."""
        if date:
            return datetime.strptime(date, "%m/%d/%Y").isoformat(' ')
        return False

    @http.route('/test', type='http', auth="public", website=True)
    def test(self, **kwargs):
        return request.render("auth_signup.signup", {})

    @http.route('/jobs/thankyou/<string:model_name>', methods=['POST'], type='http', auth="public", website=True)
    def jobs_thankyou(self, model_name, **kwargs):
        """A Method for rendering thankyou template after applying for the job.replace
        Args:
            kwargs: The second parameter to get the details of
            the job applicant.

        Returns:
            It renders the template & creates a record for job
            application also attaches the applicant's attachment to the object.

        """
        application = request.env['hr.applicant']

        env = request.env(user=SUPERUSER_ID)
        partner = env['res.partner'].sudo().browse(int(kwargs.get('partner_id')))
        job_my = env['hr.job'].sudo().search(
            [('id', '=', int(kwargs.get('job_id')))], limit=1)
        vals = {
            'source_id': 1,
            'name': kwargs.get('name') + "'s application",
            'partner_name': kwargs.get('name') or '',
            'email_from': kwargs.get('email_from'),
            'user_id': job_my.user_id.id or False,
            'academic_ids': [(6, 0, partner.academic_ids.ids)],
            'experience_ids': [(6, 0, partner.experience_ids.ids)],
            'certification_ids': [(6, 0, partner.certification_ids.ids)],
            'emergency_contact_ids': [(6, 0, partner.emergency_contact_ids.ids)],
            'country_id': partner.country_id.id,
            'partner_id': partner.id,
        }

        for field in self._get_applicant_char_fields():
            vals[field] = kwargs.get(field)

        for field in self._get_applicant_relational_fields():
            vals[field] = int(kwargs.get(field) or False)
        vals['country_id'] = kwargs.get('country_id')
        vals['street_ht'] = kwargs.get('street_ht')
        vals['street2_ht'] = kwargs.get('street2_ht')
        vals['city_ht'] = kwargs.get('city_ht')
        vals['zip_ht'] = kwargs.get('zip_ht')
        vals['state_id_ht'] = kwargs.get('state_id_ht')
        vals['marital'] = kwargs.get('marital')
        vals['gender'] = kwargs.get('gender')
        vals['birthday'] = kwargs.get('birthday')

        vals.update({
            'position_desired': kwargs.get('position_desired'),
            'other_position_desired': kwargs.get('other_position_desired'),
            # Personal
            'citizenship': kwargs.get('citizenship'),
            'driving_license': kwargs.get('driving_license'),
            'ssn': kwargs.get('ssn'),
            'citizen_restriction': kwargs.get('citizen_restriction'),

            # SKILLS/TRAININGS ATTENDED
            'skill_date_1': kwargs.get('skill_date_1'),
            'skill_name_1': kwargs.get('skill_name_1'),

            'skill_date_2': kwargs.get('skill_date_2'),
            'skill_name_2': kwargs.get('skill_name_2'),

            'skill_date_3': kwargs.get('skill_date_3'),
            'skill_name_3': kwargs.get('skill_name_3'),

            'skill_date_4': kwargs.get('skill_date_4'),
            'skill_name_4': kwargs.get('skill_name_4'),

            'cpr_expiration_date': kwargs.get('cpr_expiration_date'),
            'last_physical_exam_date': kwargs.get('last_physical_exam_date'),
            'last_xray_date': kwargs.get('last_xray_date'),          
        
            # References
            'reference_name1': kwargs.get('reference_name1'),
            'reference_name2': kwargs.get('reference_name2'),
            'reference_name3': kwargs.get('reference_name3'),
            'reference_name4': kwargs.get('reference_name4'),
            
            'reference_rln1': kwargs.get('reference_rln1'),
            'reference_rln2': kwargs.get('reference_rln2'),
            'reference_rln3': kwargs.get('reference_rln3'),
            'reference_rln4': kwargs.get('reference_rln4'),
            
            'reference_cmpny1': kwargs.get('reference_cmpny1'),
            'reference_cmpny2': kwargs.get('reference_cmpny2'),
            'reference_cmpny3': kwargs.get('reference_cmpny3'),
            'reference_cmpny4': kwargs.get('reference_cmpny4'),
            
            'reference_contact1': kwargs.get('reference_contact1'),
            'reference_contact2': kwargs.get('reference_contact2'),
            'reference_contact3': kwargs.get('reference_contact3'),
            'reference_contact4': kwargs.get('reference_contact4'),
          
            # Insurance Info
            'pl_insurance_name': kwargs.get('pl_insurance_name'),
            'pl_insurance_start_date': kwargs.get('pl_insurance_start_date'),
            'pl_insurance_end_date': kwargs.get('pl_insurance_end_date'),
            'insurance_history': kwargs.get('insurance_history'),
            'insurance_history_details': kwargs.get('insurance_history_details'),

            # General Info
            'age_validation': kwargs.get('age_validation'),
            'employed_home_health': kwargs.get('employed_home_health'),
            'means_of_transportation': kwargs.get('means_of_transportation'),
            'driving_licens': kwargs.get('driving_licens'),
            'state_driving_license': kwargs.get('state_driving_license'),
            'license_expiry': kwargs.get('license_expiry'),
            'driving_licens_revoke': kwargs.get('driving_licens_revoke'),
            'driving_license_revoke_reason': kwargs.get('driving_license_revoke_reason'),
            'task_without_accom': kwargs.get('task_without_accom'),
            'task_without_accom_reason': kwargs.get('task_without_accom_reason'),
            'facility_from_state': kwargs.get('facility_from_state'),
            'other_business': kwargs.get('other_business'),
            'other_business_reason': kwargs.get('other_business_reason'),
            'military_service': kwargs.get('military_service'),
            'law_violation': kwargs.get('law_violation'),
            'law_violation_reason': kwargs.get('law_violation_reason'),
            'hear_from': kwargs.get('hear_from'),
            
            'digital_signature': kwargs.get('digital_signature')
        })

        partner.write({
            'country_id': kwargs.get('country_id'), 'state_id': kwargs.get('state_id'),
            'city': kwargs.get('city'), 'street': kwargs.get('street'), 'street2': kwargs.get('street2'),
        })
        redundant_check = application.sudo().search(
            [('email_from', '=', kwargs.get('email_from'))], limit=1).id
        if redundant_check:
            redundant = application.sudo().search(
                [('email_from', '=', kwargs.get('email_from')), (
                    'job_id', '=', int(kwargs.get('job_id')))], limit=1).id
            if redundant:
                applicant_1 = application.sudo().search(
                    [('partner_id', '=', request.env.user.partner_id.id)],
                    limit=1, order='create_date desc')
                applicant_1.write(vals)
        applicant_id = application.sudo().create(vals).id

        for field_name in self._get_applicant_files_fields():
            if kwargs.get('field_name', None):
                attachment_vals = {
                    'name': kwargs[field_name].filename,
                    'res_name': vals['name'],
                    'res_model': 'hr.applicant',
                    'res_id': applicant_id,
                    'datas': base64.encodestring(kwargs[field_name].read()),
                }
                env['ir.attachment'].create(attachment_vals)
        return json.dumps({'id': applicant_id})
