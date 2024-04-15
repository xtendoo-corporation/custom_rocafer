# Copyright 2024 Xtendoo - Manuel Calero
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).
from odoo import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = "res.config.settings"

    h1_value_field = fields.Float(
        string='H1 Value',
        related="company_id.h1_value",
        readonly=False,
    )

    h2_value_field = fields.Float(
      #  default=coastal,
        string='H2 Value',
        # related="product_template_id.h2_value",
    )

    # frutas_dominguez_garrido_website_price_default_message = fields.Char(
    #     related="website_id.frutas_dominguez_garrido_website_price_default_message",
    #     readonly=False,
    # )
