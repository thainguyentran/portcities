# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from datetime import date
from odoo import api, fields, models
import logging

_logger = logging.getLogger(__name__)


class DeliveryRequest(models.Model):
    _name = "pcs.delivery.request"
    _description = "Delivery Request"

    name = fields.Char(string="Request Number")
    request_date = fields.Date(string="Request Date", default=date.today())
    delivery_status = fields.Selection(
        selection=[('not_ready', 'Not Ready'),
                   ('ready', 'Ready'),
                   ('in_progress', 'In Progress'),
                   ('completed', 'Completed')],
        string="Delivery Status")
    date_done = fields.Date(string="Done Date")
    delivery_details_ids = fields.One2many('pcs.delivery.details', 'dr_id', string="Delivery Detail", copy=True)

    @api.model
    def create(self, vals):
        name = str(date.today().strftime('%Y%m%d')) + self.env['ir.sequence'].next_by_code('pcs.dr.seq')
        vals.update({
            'name': name
        })
        return super(DeliveryRequest, self).create(vals)

    def complete_delivery(self):
        for dr in self:
            dr.update({'delivery_status': 'completed',
                       'date_done': date.today()})
            move = self.env['pcs.product.move']
            move_vals = {}
            for line in dr.delivery_details_ids:
                move_vals = {
                    'move_date': date.today(),
                    'product_id': line.product_id,
                    'wh_id': line.wh_id,
                    'move_qty': line.qty_requested,
                    'move_type': 'out'
                }
            move_id = move.sudo().create(move_vals)
        _logger.debug("move with move_id %s created", move_id)

    # This function is to check if the delivery request is ready or not
    @api.model
    def dr_ready(self):
        for rec in self.search([('delivery_status', '=', 'not_ready')]):
            for line in rec.delivery_details_ids:
                product = self.env['pcs.product'].search([('id', '=', line.product_id.id)])
                if line.qty_requested <= product.quantity_on_hand:
                    rec.delivery_status = 'ready'
