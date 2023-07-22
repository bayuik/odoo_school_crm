# -*- encoding: utf-8 -*-
{
    'name': 'CRM - Product Segment',
    'version': '0.1.0',
    'license': 'LGPL-3',
    'category': 'crm',
    'summary': 'CRM',
    'description': """
    CRM - Product Segment
""",
    'author': 'Bayuik',
    'website': 'https://www.bayuik.my.id/',
    'depends': ['base', 'crm', 'project'],
    'data': [
        'views/crm_lead_views.xml',
        'views/product_segment_views.xml',
        'security/ir.model.access.csv',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
