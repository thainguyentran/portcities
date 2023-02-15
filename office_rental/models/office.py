# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models
from datetime import date
import logging
_logger = logging.getLogger(__name__)


class Office(models.Model):
    _name = "or.building.office"
    _description = "Office"

    building_id = fields.Many2one("or.building", string="Building")
    name = fields.Char(string="Office", required=True)
    office_status = fields.Selection(
        selection=[('vacant', 'Vacant'), ('occupied', 'Occupied')],
        default="vacant",
        string="Office Status")

    @api.model
    def reset_office_status(self):
        for rec in self.search([('office_status', '=', 'occupied')]):
            contract = self.env['or.contract'].search([('office_id', '=', rec.id)])
            today = date.today()
            if today > contract.contract_end_date:
                rec.office_status = 'vacant'
