from odoo import api, fields, models


class ResPartner(models.Model):
    _inherit = "res.partner"

    sa_national_id = fields.Char(
        string="Saudi National ID",
        help="Optional national ID, residency ID, commercial registration, or other identity reference.",
        index=True,
        copy=False,
    )

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if vals.get("sa_national_id"):
                vals["sa_national_id"] = vals["sa_national_id"].strip()
        return super().create(vals_list)

    def write(self, vals):
        if vals.get("sa_national_id"):
            vals = dict(vals, sa_national_id=vals["sa_national_id"].strip())
        return super().write(vals)
