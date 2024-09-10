# Copyright (C) 2024 Salvador Aramis González Jiménez (<https://xtendoo.es>).
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import fields, models, api

class OperationType(models.Model):
    _name = 'operation.type'
    _description = 'Operación id'

    name = fields.Char('Operación id', required=True)

    mrp_workorder_operation_type = fields.One2many(
        comodel_name='mrp.workorder',
        inverse_name='operation_type',
        string='Operación',
    )
