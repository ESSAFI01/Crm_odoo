{
    'name': 'CRM Automation',
    'version': '16.0.1.0.0',
    'category': 'Sales/CRM',
    'summary': 'Automated CRM features with reminders and feedback',
    'description': """
        This module extends Odoo CRM with:
        - Auto-archiving of opportunities after 30 days
        - Automated reminders (7/15/30 days)
        - Customer feedback surveys
    """,
    'author': 'Chabab',
    'depends': ['base', 'crm', 'mail'],
    'data': [
        'security/ir.model.access.csv',
        'views/crm_lead_views.xml',
        'views/feedback_survey_views.xml',
    ],
    'application': True,
    'installable': True,
    'auto_install': False,
}
