# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models


class DeliveryDetails(models.Model):
    _name = "pcs.delivery.details"
    _description = "Delivery Details"

    dr_id = fields.Many2one('pcs.delivery.request', string="Delivery Request")
    product_id = fields.Many2one('pcs.product', string="Product", required=True)
    wh_id = fields.Many2one('pcs.warehouse', string="Warehouse", compute='_get_wh_id')
    qty_requested = fields.Float(string="Quantity Requested", required=True)
    qty_available = fields.Float(string="Quantity Available", related='product_id.quantity_on_hand')

    #not done yet
    def _get_wh_id(self):
        product = self.env['pcs.product']
        wh_id = product.search([('id', '=', self.product_id)], limit=1)
        return wh_id



