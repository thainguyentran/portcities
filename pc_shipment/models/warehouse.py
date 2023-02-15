# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models


class Warehouse(models.Model):
    _name = "pcs.warehouse"
    _description = "Warehouse"

    name = fields.Char(string="Name", required=True)
    address = fields.Char(string="Address", required=True)
    location = fields.Many2one('pcs.warehouse.location', string="Warehouse Location", required=True)
