from odoo import fields, models


class Kelas(models.Model):
    _name = 'sekolah.kelas'
    _description = 'Kelas'
    _order = 'name asc'

    name = fields.Char("Nama Kelas", required=True)
    siswa_ids = fields.One2many('sekolah.siswa', 'kelas_id', 'Siswa')
    wali_kelas_id = fields.Many2one('sekolah.guru', 'Guru')
