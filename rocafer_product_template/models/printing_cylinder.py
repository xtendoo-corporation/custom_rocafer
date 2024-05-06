# Copyright (C) 2024 Manuel Calero (<https://xtendoo.es>).
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import fields, models, api


class PrintingCylinder(models.Model):
    _name = "printing.cylinder"
    _description = "Printing cylinder"

    name = fields.Char(
        string="Machine name"
    )

    z_impression_cylinder = fields.Integer(
        string="Z Impression cylinder"
    )

    z_magnetic_cut = fields.Integer(
        string="Z Magnetic Cut"
    )

    printing_cylinder_line_ids = fields.One2many(
        comodel_name='printing.cylinder.line',
        inverse_name='printing_cylinder_id',
        string='Cylinder size'
    )

    @api.model
    def name_get(self):
        result = []
        for rec in self:
            name = f"[{rec.name}] {rec.z_impression_cylinder} ({rec.z_magnetic_cut})"
            result.append((rec.id, name))
        return result


class CylinderLine(models.Model):
    _name = "printing.cylinder.line"
    _description = "Cylinder line"

    printing_cylinder_id = fields.Many2one(
        comodel_name='printing.cylinder',
        string='Printing cylinder'
    )

    size = fields.Float(
        string="Value"
    )

