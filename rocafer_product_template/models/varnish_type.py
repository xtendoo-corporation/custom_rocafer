# Copyright (C) 2024 Manuel Calero (<https://xtendoo.es>).
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import fields, models, api


class VarnishType(models.Model):
    _name = "varnish.type"
    _description = "Varnish type"

    name = fields.Char(
        string="Varnish name"
    )

    product_template_varnish_type = fields.One2many(
        comodel_name='product.template',
        inverse_name='product_varnish',
        string='Varnish',
    )

