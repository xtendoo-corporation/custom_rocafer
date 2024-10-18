# Copyright (C) 2024 Salvador Aramis González Jiménez (<https://xtendoo.es>).
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import fields, models, api


class MrpWorkOrder(models.Model):
    _inherit = "mrp.workorder"

    routing_workcenter_id = fields.Many2one(
        comodel_name='workcenter.operation',
        string='Operación',
    )

    def get_operation_selection(self):
        if self.routing_workcenter_id:
            return self.routing_workcenter_id.operation_selection.name
        return False

    employee_id = fields.Many2one(
        comodel_name='hr.employee',
        string='Empleado',
    )

    date_order = fields.Datetime(
        related="sale_id.date_order",
        string="Fecha de pedido",
        store=True,
        readonly=True,
    )
