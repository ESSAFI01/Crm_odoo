{
    'name': 'CRM Automation',
    'version': '1.0',
    'depends': ['base'],
    'category': 'Sales/CRM',
    'summary': 'Automated CRM features with reminders and feedback',
    'description': """
        This module extends Odoo CRM with:
        - Auto-archiving of opportunities after 30 days
        - Automated reminders (7/15/30 days)
        - Customer feedback surveys
    """,
    'author': 'Bardin lktaf',
    'data': [
        'security/ir.model.access.csv',
        'views/my_model_views.xml',
    ],
    'installable': True,
    'auto_install': False,
}
