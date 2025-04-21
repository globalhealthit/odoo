# See LICENSE file for full copyright and licensing details.
from datetime import *
from odoo import api, fields, models
from odoo.exceptions import UserError, ValidationError
from odoo.tools.translate import _


class HrApplicant(models.Model):
    _inherit = 'hr.applicant'

    gender = fields.Selection([('male', 'Male'), ('female', 'Female')],
                              string="Gender")
    birthday = fields.Date('Date of Birth')
    marital = fields.Selection(
        [('single', 'Single'),
         ('married', 'Married'),
         ('widower', 'Widower'),
         ('divorced', 'Divorced')],
        'Marital Status')

    passport_id = fields.Char('Passport No')
    country_id = fields.Many2one('res.country')
    is_same_address = fields.Boolean('Same as Correspondence Address')
    street_ht = fields.Char('Street')
    street2_ht = fields.Char('Street2')
    city_ht = fields.Char('City')
    zip_ht = fields.Char('Zip')
    state_id_ht = fields.Many2one('res.country.state', string="State")

    academic_ids = fields.One2many('hr.academic', 'applicant_id',
                                   'Academic experiences',
                                   help="Academic experiences")
    experience_ids = fields.One2many('hr.experience', 'applicant_id',
                                     'Professional Experiences',
                                     help='Define Professional Experiences')
    certification_ids = fields.One2many('hr.certification', 'applicant_id',
                                        'Certifications',
                                        help="Certifications")

    @api.constrains('birthday')
    def validate_applicants(self):
        if not self.env.context.get('website_id'):
            if self.birthday:
                today = date.today()
                if today <= self.birthday:
                    raise ValidationError("Please enter birth date properly!")

# New fields added from pictures

#   POSITON DESIRED FIELDS

    position_desired = fields.Selection(
        [('nurse', 'Registered Nurse'),
         ('msw', 'MSW'),
         ('speech', 'Speech Therapist'),
         ('lvn', 'LVN'),
         ('physical', 'Physical Therapist'),
         ('occupation', 'Occupational Therapist'),
         ('others', 'Others')],
        'Position Desired')

    other_position_desired = fields.Char('Other Position Desired')

    # PERSONAL INFORMATION

    citizenship = fields.Char('Citizenship')
    driving_license = fields.Char('Driving License')
    ssn = fields.Char('SSN')
    citizen_restriction = fields.Selection(
        [('yes', 'Yes'),
         ('no', 'No')], 'Citizen Restriction')

    # EMERGENY INFORMATION

    emergency_contact_1 = fields.Char('Name')
    emergency_contact_2 = fields.Char('Name')
    emergency_contact_3 = fields.Char('Name')

    emergency_relation_1 = fields.Char('Relationship')
    emergency_relation_2 = fields.Char('Relationship')
    emergency_relation_3 = fields.Char('Relationship')

    emergency_phone_1 = fields.Char('Phone')
    emergency_phone_2 = fields.Char('Phone')
    emergency_phone_3 = fields.Char('Phone')

    # PROFESSIONAL LIABILITY INSURANCE

    pl_insurance_name = fields.Char('Insurance Carrier')
    pl_insurance_start_date = fields.Date('Date Began')
    pl_insurance_end_date = fields.Date('Expiration')

    insurance_history = fields.Selection(
        [('yes', 'Yes'),
        ('no', 'No')], 'Insurance History')

    insurance_history_details = fields.Char('Insurance History Details')

    # General information fields

    age_validation = fields.Selection(
        [('yes', 'Yes'),
        ('no', 'No')], 'Age validation')

    employed_home_health = fields.Selection(
        [('yes', 'Yes'),
        ('no', 'No')], 'Emplyed Home health')

    means_of_transportation = fields.Selection(
        [('yes', 'Yes'),
        ('no', 'No')], 'Means Of Transportation')

    driving_licens = fields.Selection(
        [('yes', 'Yes'),
        ('no', 'No')], 'Driving license')

    state_driving_license = fields.Char('State of License')
    license_expiry = fields.Date('Licens Expiry Date')

    driving_licens_revoke = fields.Selection(
        [('yes', 'Yes'),
        ('no', 'No')], 'Driving license Revoke')
    driving_license_revoke_reason = fields.Char('License Revoke Reason')

    task_without_accom = fields.Selection(
        [('yes', 'Yes'),
        ('no', 'No')], 'Task Accommodation')
    task_without_accom_reason = fields.Char('Task Accommodation Reason')

    facility_from_state = fields.Selection(
        [('yes', 'Yes'),
        ('no', 'No')], 'Facility From State')

    other_business = fields.Selection(
        [('yes', 'Yes'),
        ('no', 'No')], 'Other Business')
    other_business_reason = fields.Char('Other Business Reason')

    military_service = fields.Selection(
        [('yes', 'Yes'),
        ('no', 'No')], 'Military Service')

    law_violation = fields.Selection(
        [('yes', 'Yes'),
        ('no', 'No')], 'Law Violation')
    law_violation_reason = fields.Char('Law Violation Reason')

    hear_from = fields.Selection(
        [('news', 'Newspaper'),
        ('job', 'Job Fair'),
        ('website', 'Website'),
        ('emp_ref', 'Employee Referral')],
        'Hear From')

    # SKILLS/TRAININGS ATTENDED

    skill_date_1 = fields.Date('Date')
    skill_name_1 = fields.Char('Name')

    skill_date_2 = fields.Date('Date')
    skill_name_2 = fields.Char('Name')

    skill_date_3 = fields.Date('Date')
    skill_name_3 = fields.Char('Name')

    skill_date_4 = fields.Date('Date')
    skill_name_4 = fields.Char('Name')


    cpr_expiration_date = fields.Date('CPR Expiration Date')
    last_physical_exam_date = fields.Date('Last Physical Exam Date')
    last_xray_date = fields.Date('Last TB/Chest X-ray Date')

    # References

    reference_name1= fields.Char('Name')
    reference_name2= fields.Char('Name')
    reference_name3= fields.Char('Name')
    reference_name4= fields.Char('Name')

    reference_rln1= fields.Char('Relationship')
    reference_rln2= fields.Char('Relationship')
    reference_rln3= fields.Char('Relationship')
    reference_rln4= fields.Char('Relationship')

    reference_cmpny1= fields.Char('Company')
    reference_cmpny2= fields.Char('Company')
    reference_cmpny3= fields.Char('Company')
    reference_cmpny4= fields.Char('Company')


    reference_contact1= fields.Char('Contact Number')
    reference_contact2= fields.Char('Contact Number')
    reference_contact3= fields.Char('Contact Number')
    reference_contact4= fields.Char('Contact Number')



