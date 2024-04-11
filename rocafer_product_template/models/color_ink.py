# Copyright (C) 2024 Manuel Calero (<https://xtendoo.es>).
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import fields, models, api


class ColorInk(models.Model):
    _name = "color.ink"
    _description = "Color inks"

    name = fields.Char(
        string="Name",
    )

    product_template_id = fields.Many2one(
        comodel_name='product.template',
        string='Product',
    )
