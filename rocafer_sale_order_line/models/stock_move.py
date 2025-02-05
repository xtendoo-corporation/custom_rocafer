from odoo import models, api, fields

class StockMove(models.Model):
    _inherit = "stock.move"

    total_units = fields.Integer(string='Unidades totales', compute='_compute_total_units', store=True, readonly=False)

    @api.depends('product_uom_qty', 'product_uom')
    def _compute_total_units(self):
        for line in self:
            line.total_units = line.product_uom_qty * line.product_uom.ratio

    @api.onchange('total_units')
    def onchange_total_units(self):
        for line in self:
            if line.total_units:
                line.product_uom_qty = line.total_units / 1000
                line._compute_product_qty()

