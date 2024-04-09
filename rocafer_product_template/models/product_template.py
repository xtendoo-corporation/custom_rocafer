# Copyright (C) 2024 Manuel Calero (<https://xtendoo.es>).
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import fields, models, api


class Product(models.Model):
    _inherit = 'product.template'

    res_partner_id = fields.Many2one(
        comodel_name='res.partner',
        string='Name',
    )

    label_code = fields.Char(
        string='Label code'
    )

    date_order = fields.Date(
        string='Date order'
    )

    register_by = fields.Char(
        string='Register by:'
    )

    num_order = fields.Integer(
        string='Number order'
    )

    num_partner = fields.Integer(
        string='Number partner'
    )

    num_order_partner = fields.Integer(
        string='Partner order number'
    )

    troquel_number = fields.Char(
        string='Troquel number'
    )

    figures = fields.Integer(
        string='Figures'
    )

    z_imp_cor = fields.Integer(
        string='Z. IMP./COR.'
    )

    y_height = fields.Integer(
        string='Y height'
    )

    x_width = fields.Integer(
        string='X Width'
    )

    date_delivery = fields.Date(
        string='Date delivery'
    )

    amount = fields.Integer(
        string='Amount'
    )

    size = fields.Char(
        string='Size'
    )

    product_material = fields.Many2one(
        comodel_name='product.template',
        string='Product Material',
    )

    colors = fields.Integer(
        string='Colors'
        #VER COLORES PIE DE PAGINA
    )

    inner_diameter_roll = fields.Float(
        string='Inner diameter roll'
    )

    outer_diameter_roll = fields.Float(
        string='Outer diameter roll'
    )

    amount_label_exit = fields.Integer(
        string='Amount label exit'
    )

    maq_label = fields.Char(
        string='MAQ Label'
    )

    product_orientation_image = fields.Many2one(
        comodel_name='product.template',
        string='Product Orientation',
    )

    product_varnish = fields.Many2one(
        comodel_name='varnish.type',
        string='Product Varnish',
    )

    product_stamping = fields.Many2one(
        comodel_name='product.template',
        string='Product Stamping',
    )

    administration_comments = fields.Char(
        string='Administration Comments'
    )
