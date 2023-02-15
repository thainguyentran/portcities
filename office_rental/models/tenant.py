# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models


class Tenant(models.Model):
    _name = "or.tenant"
    _description = "Tenant"

    name = fields.Char("Name", required=True)
    phone_num = fields.Char("Phone Number", required=True)
    email = fields.Char("Email", required=True)
