from odoo import models, api, fields
from odoo.tools import float_is_zero, float_compare, float_round, format_date, groupby

class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    total_units = fields.Integer(string='Unidades totales', compute='_compute_total_units')

    @api.depends('product_uom_qty', 'product_uom')
    def _compute_total_units(self):
        for line in self:
            line.total_units = line.product_uom_qty * line.product_uom.ratio

    @api.depends('display_type', 'product_id', 'product_packaging_qty', 'total_units')
    def _compute_product_uom_qty(self):
        for line in self:
            if line.total_units:
               line.product_uom_qty = line.total_units / line.product_uom.ratio
            else:
                if line.display_type:
                    line.product_uom_qty = 0.0
                    continue

                if not line.product_packaging_id:
                    continue
                packaging_uom = line.product_packaging_id.product_uom_id
                qty_per_packaging = line.product_packaging_id.qty
                product_uom_qty = packaging_uom._compute_quantity(
                    line.product_packaging_qty * qty_per_packaging, line.product_uom)
                if float_compare(product_uom_qty, line.product_uom_qty, precision_rounding=line.product_uom.rounding) != 0:
                    line.product_uom_qty = product_uom_qty

    assembly_figure_x_from_product_template = fields.Integer(
        string='Assembly figure x',
        related='product_id.assembly_figure_x',
    )

    printing_cylinder_size_from_product_template = fields.Float(
        string='Printing cylinder size',
        related='product_id.printing_cylinder_size',
    )

    tolerance_from_product_template = fields.Float(
        string='Tolerance',
        related='product_id.tolerance',
    )

    linear_meters = fields.Float(
        string='Linear meters',
        compute='_compute_meters',
        store=True
    )

    @api.depends('assembly_figure_x_from_product_template', 'printing_cylinder_size_from_product_template',
                 'tolerance_from_product_template', 'product_uom_qty')
    def _compute_meters(self):
        self.linear_meters = 0
        for record in self.filtered(lambda r: r.assembly_figure_x_from_product_template):
            if record.tolerance_from_product_template == 0:
                record.linear_meters = round((
                                                   record.product_uom_qty / 1000 * record.printing_cylinder_size_from_product_template) / record.assembly_figure_x_from_product_template)
            else:
                record.linear_meters = round((
                                                   record.product_uom_qty / 1000 * record.printing_cylinder_size_from_product_template) / record.assembly_figure_x_from_product_template * (
                                                   1 + record.tolerance_from_product_template / 100))

    # @api.depends('assembly_figure_x_from_product_template', 'printing_cylinder_size_from_product_template', 'tolerance_from_product_template', 'product_uom_qty')
    # def _compute_meters(self):
    #     self.linear_meters = 0
    #     for record in self.filtered(lambda r: r.assembly_figure_x_from_product_template):
    #         if (record.tolerance_from_product_template == 0):
    #             record.linear_meters = (record.product_uom_qty / 1000 * record.printing_cylinder_size_from_product_template) / record.assembly_figure_x_from_product_template
    #         else:
    #             record.linear_meters = (record.product_uom_qty / 1000 * record.printing_cylinder_size_from_product_template) / record.assembly_figure_x_from_product_template * (1 + record.tolerance_from_product_template / 100)
