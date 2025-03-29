from odoo import api, fields, models


class Note(models.Model):
    _inherit = "note.note"

    name = fields.Text(compute="_compute_name", string="Note Summary", readonly=False)
