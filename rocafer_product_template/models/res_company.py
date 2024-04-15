# -*- coding: utf-8 -*-

from odoo import models, fields


class res_company(models.Model):
    _inherit = "res.company"

    h1_value = fields.Float(
        string='H1 Value',
        default=3.00,
    )
