# Copyright 2019-20 ForgeFlow S.L. (https://www.forgeflow.com)
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html).

from odoo import models, fields


class MrpWorkOrder(models.Model):
    _inherit = "mrp.workorder"

    sale_order_id = fields.Many2one(
        comodel_name="sale.order",
        string="Orden de Venta",
        domain="[('name', '=', self.production_id.origin.split('-')[1] if '-' in self.production_id.origin else self.production_id.origin)]",
    )

    # sale_order_id = fields.Many2one(
    #     comodel_name="sale.order",
    #     string="Orden de Venta",
    # )

    employee_id = fields.Many2one(
        comodel_name="hr.employee",
        string="Empleado",
    )
