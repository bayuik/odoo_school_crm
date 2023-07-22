from odoo import fields, models


class MataPelajaran(models.Model):
    _name = 'sekolah.mata.pelajaran'
    _description = 'Mata Pelajaran'
    _order = 'name asc'

    name = fields.Char('Nama Mata Pelajaran', required=True)
    jurusan = fields.Char('Jurusan')
