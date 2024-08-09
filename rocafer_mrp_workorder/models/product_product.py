# Copyright (C) 2024 Salvador Aramis González Jiménez (<https://xtendoo.es>).
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import models, api


class ProductProduct(models.Model):
    _inherit = 'product.product'

    def _create_orderpoints(self, product):
        warehouse = self.env['stock.warehouse'].search([], limit=1)
        orderpoint = {
            'product_min_qty': 0,
            'product_max_qty': 0,
            'qty_multiple': 0,
            'warehouse_id': warehouse.id,
            'location_id': warehouse.lot_stock_id.id,
            'product_id': product.id,
            # rute to mrp
            'route_id': self.env.ref('mrp.route_warehouse0_manufacture').id,
        }
        self.env['stock.warehouse.orderpoint'].create(orderpoint)

    @api.model
    def create(self, vals):
        record = super().create(vals)
        if record.detailed_type == 'product':
            self._create_orderpoints(record)
        return record
