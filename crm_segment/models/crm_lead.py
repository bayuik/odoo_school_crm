from odoo import fields, models, api, _


class Lead(models.Model):
    _inherit = 'crm.lead'

    is_new_customer = fields.Boolean('Is New Customer')
    customer_segment = fields.Selection([
        ('konstruksi', 'Konstruksi'), ('perbankan', 'Perbankan'), ('pemerintah', 'Pemerintah'), ('bumn', 'BUMD/BUMN'),
        ('pemerintahan', 'Pemerintahan'), ('swasta', 'Swasta'), ('lainnya', 'Lainnya')
    ], 'Customer Segment')
    product_segment_id = fields.Many2one('product.segment', 'Product Segment')
