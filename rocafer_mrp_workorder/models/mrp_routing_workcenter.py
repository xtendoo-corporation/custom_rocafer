# Copyright (C) 2024 Salvador Aramis González Jiménez (<https://xtendoo.es>).
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import fields, models, api, _


class MrpRoutingWorkcenterInherit(models.Model):
    _inherit = 'mrp.routing.workcenter'

    operation_selection = fields.Many2one(
        'workcenter.operation',
        string='Operación',
    )

    @api.onchange('operation_selection')
    def _onchange_operation_selection(self):
        if self.operation_selection:
            self.name = self.operation_selection.name
