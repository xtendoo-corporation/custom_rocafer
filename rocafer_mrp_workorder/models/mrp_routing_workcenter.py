# Copyright (C) 2024 Salvador Aramis González Jiménez (<https://xtendoo.es>).
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import fields, models, api, _


class MrpRoutingWorkcenterInherit(models.Model):
    _inherit = 'mrp.routing.workcenter'

    operation_selection = fields.Many2one(
        comodel_name='workcenter.operation',
        string='Operación',
    )

    time_cycle_manual = fields.Float(
        'Manual Duration', default=00.00,
        help="Time in minutes:"
        "- In manual mode, time used"
        "- In automatic mode, supposed first time when there aren't any work orders yet"
    )

    @api.onchange('operation_selection')
    def _onchange_operation_selection(self):
        for record in self:
            if record.operation_selection:
                record.name = record.operation_selection.name
