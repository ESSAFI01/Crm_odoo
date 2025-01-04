from odoo import models, fields, api

class FeedbackSurvey(models.Model):
    _name = 'feedback.survey'
    _description = 'Customer Feedback Survey'

    name = fields.Char(string='Survey Name', required=True)
    customer_name = fields.Char(string='Customer Name')
    rating = fields.Selection([
        ('1', 'Very Unsatisfied'),
        ('2', 'Unsatisfied'),
        ('3', 'Neutral'),
        ('4', 'Satisfied'),
        ('5', 'Very Satisfied')
    ], string='Satisfaction Rating')
    feedback_text = fields.Text(string='Feedback Details')
    date_submitted = fields.Datetime(string='Submission Date', default=fields.Datetime.now)