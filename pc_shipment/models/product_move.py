# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from datetime import datetime, date
from odoo import models, fields, api, time, _
from odoo.exceptions import UserError, ValidationError
import logging
_logger = logging.getLogger(__name__)


class ProductMove(models.Model):
    _name = "pcs.product.move"
    _description = "Product Move"

    move_date = fields.Date(default=date.today())
    product_id = fields.Many2one('pcs.product', string="Product", required=True)
    wh_id = fields.Many2one('pcs.warehouse', string="Warehouse", required=True)
    move_qty = fields.Float(string="Quantity Move", store=True, required=True)
    move_type = fields.Selection(
        selection=[('in', 'In'), ('out', 'Out')],
        default='in',
        required=True,
        string='Move Type')
    move_status = fields.Selection(
        selection=[('draft', 'draft'), ('done', 'Done')],
        default='draft',
        string='Move Status')

    @api.model
    def create(self, vals):
        today = date.today()
        mv_date = date.today()
        if isinstance(vals["move_date"], str):
            mv_date = datetime.strptime(vals["move_date"], '%Y-%m-%d').date()
        if mv_date > today:
            raise UserError(_("Move Date cannot be in the future"))
        vals['move_status'] = 'done'
        res = super(ProductMove, self).create(vals)
        return res
