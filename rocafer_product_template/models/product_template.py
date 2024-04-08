# Copyright (C) 2024 Manuel Calero (<https://xtendoo.es>).
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import fields, models, api


class Product(models.Model):
    _inherit = 'product.template'

    # Elegir entre los pructos creados
    res_partner_id = fields.Many2one(
        comodel_name='res.partner',
        string='Name',
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

    troquel_number = fields.Integer(
        string='Troquel number'
    )
    figures = fields.Integer(
        string='Figures'
    )
    z_imp_cor = fields.Integer(
        string='Z. IMP./COR.'
    )
    meters = fields.Integer(
        string='Meters'
    )
    width = fields.Integer(
        string='Width'
    )
    time_estimated = fields.Integer(
        string='Time Estimated'
    )
    assembly_figures = fields.Integer(
        string='Assembly figures'
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
    material = fields.Char(
        string='***TABLA DE MATERIALES***'
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
    orientation_image = fields.Char(
        string='***TABLA DE IMAGENES***'
    )
    varnish = fields.Char(
        string='***TABLA DE BARNICES***'
    )
    extrampation = fields.Char(
        string='***TABLA DE ESTAMPACIONES***'
    )




