# Copyright (C) 2024 Salvador Aramis González Jiménez (<https://xtendoo.es>).
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import fields, models, api

class MrpRoutingWorkcenter(models.Model):
    _name = "mrp.routing.workcenter"
    _description = "Mrp Routing Workcenter"

    name = fields.Char(
        string="Mrp Routing Workcenter"
    )

    mrp_workorder_routing = fields.One2many(
        comodel_name='mrp.workorder',
        inverse_name='name',
        string='Operación',
    )
