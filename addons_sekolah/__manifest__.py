# -*- encoding: utf-8 -*-
{
    'name': 'Sekolah',
    'version': '0.1.0',
    'license': 'LGPL-3',
    'category': 'crm',
    'summary': 'sekolah',
    'description': """
""",
    'author': 'Bayuik',
    'website': 'https://www.bayuik.my.id/',
    'depends': ['base'],
    'data': [
        'views/guru_views.xml',
        'views/jadwal_views.xml',
        'views/kelas_views.xml',
        'views/mata_pelajaran_views.xml',
        'views/siswa_views.xml',
        'views/menus.xml',
        'security/sekolah_security.xml',
        'security/ir.model.access.csv',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
