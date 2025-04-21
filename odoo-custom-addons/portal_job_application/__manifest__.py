{
    'name': 'Portal Job Application',
    'version': '1.0',
    'category': 'Human Resources',
    'summary': 'Allows portal users to view their job application status',
    'depends': ['hr_recruitment', 'portal', 'website'],
    'data': [
        'views/portal_job_application_templates.xml',
    ],
    'installable': True,
    'application': False,
    'license': 'LGPL-3',
}
