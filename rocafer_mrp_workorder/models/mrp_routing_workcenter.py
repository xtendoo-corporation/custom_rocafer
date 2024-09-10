# Copyright (C) 2024 Salvador Aramis González Jiménez (<https://xtendoo.es>).
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import fields, models, api, _


class MrpRoutingWorkcenter(models.Model):
    _inherit = 'mrp.routing.workcenter'

    # operation_id = fields.Many2one(
    #     'operation.type',
    #     string='Operación id',
    #     required=True,
    #     store=True,
    # )

    operation_selection = fields.Many2one(
        'mrp.routing.workcenter',
        string='Operación',
        domain=['|', ('bom_id', '=', False), ('bom_id.active', '=', True)],
    )

    @api.onchange('operation_selection')
    def _onchange_operation_selection(self):
        if self.operation_selection:
            self.name = self.operation_selection


    # def copy_existing_operations(self):
    #     return {
    #         'type': 'ir.actions.act_window',
    #         'name': _('Select Operations to Copy'),
    #         'res_model': 'mrp.routing.workcenter',
    #         'view_mode': 'tree,form',
    #         'domain': ['|', ('bom_id', '=', False), ('bom_id.active', '=', True)],
    #         'context' : {
    #             'bom_id': self.env.context["bom_id"],
    #             'tree_view_ref': 'mrp.mrp_routing_workcenter_copy_to_bom_tree_view',
    #         }
    #     }
