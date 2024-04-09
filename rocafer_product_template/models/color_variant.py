# Copyright (C) 2024 Manuel Calero (<https://xtendoo.es>).
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import fields, models, api


class ColorVariant(models.Model):
    _name = "color.variant"
    _description = "Color variant"

    name = fields.Char(
        string="Color variant"
    )

    product_template_color_variant = fields.One2many(
        comodel_name='product.template',
        inverse_name='color_variant',
        string='Color',
    )
