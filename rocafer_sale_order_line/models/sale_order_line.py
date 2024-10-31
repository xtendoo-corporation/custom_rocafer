from odoo import models, api, fields

class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    total_units = fields.Integer(string='Unidades totales', compute='_compute_total_units', store=True)

    @api.depends('product_uom_qty')
    def _compute_total_units(self):
        for line in self:
            line.total_units = line.product_uom_qty * 1000

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
