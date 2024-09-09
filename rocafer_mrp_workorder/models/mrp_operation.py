# Copyright (C) 2024 Salvador Aramis González Jiménez (<https://xtendoo.es>).
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import fields, models, api

class MrpOperation(models.Model):
    _name = "mrp.routing.workcenter"
    _description = "Mrp Operation"

    name = fields.Char(
        string="Mrp Operation"
    )

    mrp_workorder_operation = fields.One2many(
        comodel_name='mrp.workorder',
        inverse_name='name',
        string='Operación',
    )
