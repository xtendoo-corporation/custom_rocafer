# Copyright (C) 2024 Manuel Calero (<https://xtendoo.es>).
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import fields, models, api


class PrintingCylinder(models.Model):
    _name = "printing.cylinder"
    _description = "Printing cylinder"

    name = fields.Char(
        string="Machine name"
    )

    z_impression_cylinder = fields.Char(
        string="Z Impression cylinder"
    )

    z_magnetic_cut = fields.Char(
        string="Z Magnetic Cut"
    )

    printing_cylinder_line = fields.One2many(
        comodel_name='printing.cylinder.line',
        inverse_name='value',
        string='Cylinder size'
    )


class CylinderLine(models.Model):
    _name = "printing.cylinder.line"
    _description = "Cylinder line"

    value = fields.Integer(
        string="Value"
    )

    #--------------------------------------------ANTIGUO------------------------------------------------------
    #el campo a calcular se muestra en
    #advance_label_separation

    # @api.depends('colum_1', 'colum_2', 'colum_3', 'colum_4', 'colum_5', 'colum_6', 'colum_7', 'colum_8', 'colum_9', 'colum_10', 'colum_11', 'colum_12', 'colum_13', 'colum_14')
    # def _compute_correct_size(self):
    #     for record in self:
    #         values = [record[f'colum_{i}'] for i in range(1, 15)]
    #         values.sort()
    #         for value in range(0, len(values)):
    #             if value >= record.correct_size:
    #                 if value == record.correct_size:
    #                     closest_greater = value
    #
    #         if closest_greater is None:
    #             record.correct_size = 0
    #         else:
    #             record.correct_size = closest_greater


