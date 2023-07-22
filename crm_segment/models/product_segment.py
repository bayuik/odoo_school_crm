from odoo import fields, models, api, _

class ProductSegment(models.Model):
    _name = "product.segment"
    _description = 'Product Segment'
    _order = 'id asc'

    name = fields.Char('Name')
