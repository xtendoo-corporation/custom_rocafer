# Copyright (C) 2024 Manuel Calero (<https://xtendoo.es>).
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import fields, models, api


class Stamping(models.Model):
    _name = "stamping.option"
    _description = "Stamping"

    name = fields.Char(
        string="Stamping name"
    )

    product_template_varnish_type = fields.One2many(
        comodel_name='product.template',
        inverse_name='product_stamping',
        string='Stamping',
    )

