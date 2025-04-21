# See LICENSE file for full copyright and licensing details.
from datetime import *
import re
from odoo import api, fields, models,_
from odoo.exceptions import ValidationError

import json
from odoo.exceptions import AccessError, UserError
import logging
_logger = logging.getLogger(__name__)

class HrJobLevel(models.Model):
    _name = "hr.job.level"
    _description = "Job Level"

    name = fields.Char('Job Type')

class HrJobSector(models.Model):
    _name = "hr.job.sector"
    _description = "Job Sector"

    name = fields.Char('Sector')
    
# class ResUsers(models.Model):
#     _inherit = 'res.users'
    # is_member = fields.Boolean(string="Is Member",default=False)
    # req_id = fields.Many2one('employer.base','Employer Source')

class HrJob(models.Model):
    _inherit = 'hr.job'

    @api.model
    def _default_address_id(self):
        return self.env.user.partner_id

    address_id = fields.Many2one(
        'res.partner', "Job Location", default=_default_address_id,
        domain="['|', ('company_id', '=', False), ('company_id', '=', company_id)]",
        help="Address where employees are working", required=True)
    
    job_sector_id = fields.Many2one('hr.job.sector', "Sector", tracking=True,required=True)
    job_views_count = fields.Integer("Website View Count")
    user_id = fields.Many2one('res.users', "Responsible", domain="[('is_member','=',True)]",tracking=True,required=True,default=lambda self: self.env.user)
    # job_section_id = fields.Many2one('custom.job.section', string='Job Section',required=True)
    job_type = fields.Selection([('fulltime', 'Full Time'),('parttime', 'PartTime')], default='fulltime', string="Job Type",track_visibility='onchange')
    closing_date = fields.Date('Expiry Date',required=True)
    job_level_id = fields.Many2one('hr.job.level', string='Job Level',required=False)
    offered_salary_type = fields.Selection([('nego', 'Negotiable'),('range', 'Range'),('fixed', 'Fixed')], default='nego', string="Offered Salary Type",track_visibility='onchange')
    min_salary = fields.Float('Min')
    max_salary = fields.Float('Max')
    fix_salary = fields.Float('Fixed')
    

    study_field = fields.Selection(
        [('slc', 'SLC/SEE'),
         ('plus', '+2'),
         ('bachelor', 'Bachelor'),
         ('master', 'Master'),
         ('Phd', 'Doctorate')],
        'Level',required=True)
    # education_level = fields.Selection([('school', 'School'),('inter', 'Intermediate'),('bachelors', 'Bachelors'),('masters', 'Master'),('phd', 'PHD')], default='school', string="Education Level",track_visibility='onchange')
    experience_req = fields.Float('Experience Required (Yrs)',required=True)
    skill_ids = fields.Many2many('hr.my.skills',string='Skills Required',required=True)
    
    
    @api.model 
    def create(self,vals):
        user = vals.get('user_id')
        _logger.info("==============user====id====%s",user)
        if user == 2:
            raise UserError(
                        _(
                            "Please Change the Responsible User From 'Administrator' to Available Employers "
                            
                        )
                    )
                        

        res = super(HrJob,self).create(vals)
        return res
    

    def get_jb_details(self):
        for rec in self:
            res = []
            if rec.user_id:
                # if rec.user_id.req_id:
                    mobile = ""
                    phone = ""
                    if rec.user_id.partner_id.mobile:
                        mobile += rec.user_id.partner_id.mobile 
                    if rec.user_id.partner_id.phone:
                        phone += rec.user_id.partner_id.phone
                    res.append({
                    # 'des': rec.user_id.req_id.description,
                        # 'lnk' : rec.user_id.req_id.get_logo_url(),
                        'req_mail' : rec.user_id.partner_id.email,
                        'req_website' : rec.user_id.partner_id.website,
                        'req_name' : rec.user_id.partner_id.name,
                        'req_phone' : phone  + " ," + mobile,
                        })
                    _logger.info("------desc---%s",res)
            return res
    def get_jb_url(self):
        for rec in self:
            btx = self.env['ir.config_parameter'].get_param('web.base.url')
            return btx + '/jobs/detail/' + str(rec.id)

    @api.constrains('closing_date')
    def validate_dates(self):
        if not self.env.context.get('website_id'):
            today = date.today()
            if today >= self.closing_date:
                raise ValidationError("Closing date should be greater than"
                                      " Current Date.")

class HrMySkills(models.Model):
    _name = "hr.my.skills"
    _description = "Job Skills"

    name = fields.Char('Skill Name')
    

