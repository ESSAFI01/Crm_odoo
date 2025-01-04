{
    'name': 'CRM Automation',
    'version': '1.0',
    'depends': ['base','crm','mail'],
    'category': 'Sales/CRM',
    'summary': 'Automated CRM features with reminders and feedback',
    'description': """
        This module enhances the Odoo CRM with:
        - Automatic archiving of opportunities 30 days after their creation.
        - Automated email reminders for leads and salespeople at 7, 15, and 30 days.
        - Customer feedback collection through surveys after key activities.
    """,
    'author': 'Bardin lktaf',
    'data': [
    'security/ir.model.access.csv', 
    'views/my_model_views.xml',     
    'data/cron_jobs.xml',            
    'data/email_templates.xml',      
    ],
    'installable': True,
    'auto_install': False,
}
