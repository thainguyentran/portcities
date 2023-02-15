# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models


class Location(models.Model):
    _name = "pcs.warehouse.location"
    _description = "Warehouse's Location"

    name = fields.Char(string="Location Name", required=True)

