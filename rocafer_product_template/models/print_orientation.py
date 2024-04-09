# Copyright (C) 2024 Manuel Calero (<https://xtendoo.es>).
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import fields, models, api


class PrintOrientation(models.Model):
    _name = "print.orientation"
    _description = "Print Orientations"

    name = fields.Char(
            string="Name"
    )

    image = fields.Char(
        string="Image"
    )

    product_template_ids = fields.One2many(
        comodel_name='product.template',
        inverse_name='print_orientation_id',
        string='Productos'
    )

