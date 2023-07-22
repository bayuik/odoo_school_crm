from odoo import fields, models


class Siswa(models.Model):
    _name = 'sekolah.siswa'
    _description = 'Siswa'
    _order = 'nis, name asc'

    nis = fields.Char('NIS', required=True)
    name = fields.Char("Nama Siswa", required=True)
    jns_kelamin = fields.Selection([('laki-laki', 'Laki-Laki'), ('perempuan', 'Perempuan')], string="Jenis Kelamin")
    tgl_lahir = fields.Date("Tanggal Lahir")
    agama = fields.Selection(
        [('islam', 'Islam'), ('kristen', 'Kristen'), ('katolik', 'Katolik'), ('hindu', 'Hindu'), ('budha', 'Budha')])
    nm_ayah = fields.Char("Nama Ayah")
    nm_ibu = fields.Char("Nama Ibu")
    usia = fields.Integer("Usia", compute='_compute_usia')
    alamat = fields.Text("Alamat")
    kelas_id = fields.Many2one('sekolah.kelas', 'Kelas')

    def _compute_usia(self):
        for rec in self:
            rec.usia = rec.tgl_lahir and (fields.Date.today() - rec.tgl_lahir).days / 365 or 0