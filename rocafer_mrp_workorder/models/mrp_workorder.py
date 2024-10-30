# Copyright (C) 2024 Salvador Aramis González Jiménez (<https://xtendoo.es>).
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
from odoo import fields, models, api


class MrpWorkOrder(models.Model):
    _inherit = "mrp.workorder"

    workcenter_operation_id = fields.Many2one(
        comodel_name='workcenter.operation',
        string='Tipo de operación',
    )

    @api.onchange('workcenter_operation_id')
    def _onchange_workcenter_operation_id(self):
        for record in self:
            if record.workcenter_operation_id:
                record.name = record.workcenter_operation_id.name

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

    def _assign_workcenter_operation(self, values_list):
        for values in values_list:
            operation_id = self.env['mrp.routing.workcenter'].browse(values["operation_id"])
            if operation_id:
                values["workcenter_operation_id"] = operation_id.workcenter_operation_id.id

    @api.model_create_multi
    def create(self, values_list):
        self._assign_workcenter_operation(values_list)
        return super().create(values_list)
