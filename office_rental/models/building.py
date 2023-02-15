# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models
import logging
_logger = logging.getLogger(__name__)

class Building(models.Model):
    _name = "or.building"
    _description = "Building"

    name = fields.Char(string="Name", required=True)
    address = fields.Char(string="Address", required=True)
    office_ids = fields.One2many("or.building.office", "building_id", string="Office", copy=True)

