import re

from odoo import _, api, fields, models
from odoo.exceptions import ValidationError


class ResPartner(models.Model):
    _inherit = "res.partner"

    sa_national_id = fields.Char(
        string="Saudi National ID",
        help="Optional 10-digit Saudi national ID or residency ID.",
        index=True,
        copy=False,
    )

    @api.constrains("sa_national_id")
    def _check_sa_national_id(self):
        for partner in self:
            value = (partner.sa_national_id or "").strip()
            if not value:
                continue
            if not re.fullmatch(r"[12][0-9]{9}", value):
                raise ValidationError(
                    _(
                        "Saudi National ID must contain exactly 10 digits and "
                        "start with 1 or 2."
                    )
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
