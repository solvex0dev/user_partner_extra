# Copyright 2023 ForgeFlow, S.L.
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from odoo import _, api, fields, models
from odoo.exceptions import ValidationError


class ResPartnerCategory(models.Model):
    _inherit = "res.partner"

    partner_nis=fields.Char("N.I.S")
    partner_nif=fields.Char("N.I.F")
    partner_ai=fields.Char("A.I")
    
