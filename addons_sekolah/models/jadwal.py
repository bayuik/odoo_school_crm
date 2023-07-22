from odoo import fields, models


class Jadwal(models.Model):
    _name = 'sekolah.jadwal'
    _description = 'Jadwal'
    _order = 'hari, jam asc'

    hari = fields.Selection(
        [('senin', 'Senin'), ('selasa', 'Selasa'), ('rabu', 'Rabu'), ('kamis', 'Kamis'), ('jumat', 'Jumat'),
         ('sabtu', 'Sabtu')], "Hari", required=True)
    kelas_id = fields.Many2one('sekolah.kelas', 'Kelas', required=True)
    jam = fields.Float("Jam", required=True)
    mata_pelajaran = fields.Many2one('sekolah.mata.pelajaran', 'Mata Pelajaran', required=True)

    def name_get(self):
        result = []
        for jadwal in self:
            name = f"{jadwal.kelas_id.name}/{jadwal.hari}"
            result.append((jadwal.id, name))
        return result
