# Copyright (C) 2024 Salvador Aramis González Jiménez (<https://xtendoo.es>).
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import fields, models, api, _


class WorkcenterOperation(models.Model):
    _name = 'workcenter.operation'
    _description = 'Operaciones'

    name = fields.Char('Operación', required=True)
