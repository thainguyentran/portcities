# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from datetime import date
from odoo import api, fields, models
import logging
_logger = logging.getLogger(__name__)


class Contract(models.Model):
    _name = "or.contract"
    _description = "Contract"

    name = fields.Char(string="Contract Number")
    tenant_id = fields.Many2one("or.tenant", required=True)
    office_id = fields.Many2one(
        "or.building.office",
        required=True,
        default=lambda self: self.env['or.building.office'].search([('office_status', '=', 'vacant')]),
    )
    contract_start_date = fields.Date(string="Start Date", required=True)
    contract_end_date = fields.Date(string="End Date", required=True)
    contract_term = fields.Text(string="Contract Term")

    @api.model
    def create(self, vals):
        name = str(date.today().strftime('%Y%m%d')) + self.env['ir.sequence'].next_by_code('or.contract.seq')
        vals.update({
            'name': name
        })
        office = self.env['or.building.office'].search([('id', '=', vals['office_id'])], limit=1)
        try:
            office.office_status = 'occupied'
        except Exception:
            _logger.debug("An exception occurred")
        return super(Contract, self).create(vals)

    def get_all_contracts(self):
        return self.search([]).ids
