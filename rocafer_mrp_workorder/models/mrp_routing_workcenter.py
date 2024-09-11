# Copyright (C) 2024 Salvador Aramis González Jiménez (<https://xtendoo.es>).
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import fields, models, api, _


class MrpRoutingWorkcenter(models.Model):
    _inherit = 'mrp.routing.workcenter'

    operation_selection = fields.Many2one(
        'mrp.routing.workcenter',
        string='Elegir operación',
        domain=['|', ('bom_id', '=', False), ('bom_id.active', '=', True)],
    )

    @api.onchange('operation_selection')
    def _onchange_operation_selection(self):
        if self.operation_selection:
            self.name = self.operation_selection.name
