# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models, _
from odoo.exceptions import UserError, ValidationError
import logging
_logger = logging.getLogger(__name__)


class Product(models.Model):
    _name = "pcs.product"
    _description = "Product"

    name = fields.Char(string="Name", required=True)
    code = fields.Char(string="Code", required=True)
    product_move_ids = fields.One2many('pcs.product.move', 'product_id', help='Technical: used to compute quantities.')
    quantity_on_hand = fields.Float(
        string="Quantity On Hand",
        compute='_compute_quantity_avail',
        store=True,
        default=0.0)

    @api.onchange('product_move_ids.move_qty')
    @api.depends('product_move_ids.move_qty')
    def _compute_quantity_avail(self):
        for product in self:
            qty = 0
            move_m = self.env['pcs.product.move']
            move_ids = move_m.search([('product_id', '=', self.id)]).ids
            move_obj = move_m.browse(move_ids)
            for move in move_obj:
                if product.quantity_on_hand != 0:
                    qty = product.quantity_on_hand
                    if move.move_type == 'in':
                        qty += move.move_qty
                    else:
                        if move.move_qty <= qty:
                            qty -= move.move_qty
                        else:
                            raise UserError(_("Cannot move more than available quantity"))
                else:
                    qty = move.move_qty
            product.update({'quantity_on_hand': qty})

    _sql_constraints = [
        (
            "name_code_unique",
            "unique(name, code)",
            "This product code already exists for this product!",
        )
    ]

    @api.model
    def create(self, vals):
        res = super(Product, self).create(vals)
        return res
