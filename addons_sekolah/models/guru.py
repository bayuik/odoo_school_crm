from odoo import fields, models


class Guru(models.Model):
    _name = 'sekolah.guru'
    _description = 'Guru'
    _order = 'nip, name asc'

    name = fields.Char('Nama Guru', required=True)
    nip = fields.Char('NIP', required=True)
    jns_kelamin = fields.Selection([('laki-laki', 'Laki-Laki'), ('perempuan', 'Perempuan')], 'Jenis Kelamin')
    mata_pelajaran_id = fields.Many2one('sekolah.mata.pelajaran', 'Mata Pelajaran', required=True)
    tgl_lahir = fields.Date("Tanggal Lahir")
    usia = fields.Integer('Usia', compute="_compute_usia")
    no_telp = fields.Char('No. Telp')
    alamat = fields.Text('Alamat')

    def _compute_usia(self):
        for rec in self:
            rec.usia = rec.tgl_lahir and (fields.Date.today() - rec.tgl_lahir).days / 365 or 0
