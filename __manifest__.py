{
    'name': 'CRM Automation',
    'version': '1.0',
    'depends': ['base', 'crm', 'mail'],
    'category': 'Sales/CRM',
    'summary': 'Automated CRM features with reminders and feedback',
    'description': """
        Enhance your CRM module with automation:
        - Automatic archiving of opportunities 30 days after creation.
        - Email reminders for leads and salespeople.
        - Feedback surveys for customers to improve service quality.
    """,
    'author': 'Bardin lktaf',
    'website': 'https://yourwebsite.com',
    'data': [
        'security/ir.model.access.csv',
        'views/my_model_views.xml',
        'data/cron_jobs.xml',
        'data/email_templates.xml',
    ],
    'demo': [
        'demo/demo_data.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}
