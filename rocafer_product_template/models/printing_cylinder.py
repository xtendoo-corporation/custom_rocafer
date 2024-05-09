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

    @api.depends('name', 'z_impression_cylinder', 'z_magnetic_cut')
    def _compute_display_name(self):
        for record in self:
            record.display_name = f"{record.name} - {record.z_impression_cylinder} - {record.z_magnetic_cut}"


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

