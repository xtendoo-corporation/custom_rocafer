# Copyright (C) 2024 Manuel Calero (<https://xtendoo.es>).
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import fields, models, api


class Product(models.Model):
    _inherit = 'product.template'

    res_partner_id = fields.Many2one(
        comodel_name='res.partner',
        string='Name',
    )

    # num_partner = fields.Integer(
    #     string='Number partner'
    # )

    # num_order_partner = fields.Integer(
    #     string='Partner order number'
    # )

    label_code = fields.Char(
        string='Label code'
    )

    # date_order = fields.Date(
    #     string='Date order'
    # )
    #
    # delivery_date = fields.Date(
    #     string='Delivery date'
    # )

    # register_by = fields.Char(
    #     string='Register by:'
    # )
    #
    # num_order = fields.Integer(
    #     string='Number order'
    # )

    troquel_number = fields.Char(
        string='Troquel number'
    )

    assembly_figure_x = fields.Integer(
        string='Y height'
    )

    assembly_figure_y = fields.Integer(
        string='X Width'
    )

    troquel_figure = fields.Integer(
        string="Figures",
        compute="_calculate_troquel_figure",
        store=True,
    )

    @api.depends('assembly_figure_x', 'assembly_figure_y')
    def _calculate_troquel_figure(self):
        for record in self:
            record.troquel_figure = record.assembly_figure_x * record.assembly_figure_y

    printing_cylinders = fields.Integer(
        string='Printing cylinders'
    )

    cut_cylinders = fields.Integer(
        string='Cut cylinders'
    )

    label_width = fields.Float(
        string='Label width'
    )

    label_height = fields.Float(
        string='Label height'
    )

    h1_value = fields.Float(
        string='H1 Value',
    )

    h2_value = fields.Float(
        string='H2 Value',
    )

    amount = fields.Float(
        string='Amount',
    )

    amount_labels = fields.Float(
        string='Amount labels',
        compute='_calculate_amount',
        store=True
    )

    @api.onchange('amount', 'advance_label_separation')
    def _calculate_amount(self):
        for record in self:
            record.amount_labels = record.amount / 1000.00 * record.advance_label_separation

    advance_label_separation = fields.Float(
        string='Advance label separation',
        compute='_calculate_advance_label_separation',
        store=True
    )

    @api.depends('label_width', 'h1_value')
    def _calculate_advance_label_separation(self):
        for record in self:
            record.advance_label_separation = record.label_width + record.h1_value

    material_width_separation = fields.Float(
        string='Material width separation',
        compute='_calculate_material_width_separation',
        store=True
    )

    @api.depends('label_height', 'assembly_figure_x', 'h1_value', 'h2_value')
    def _calculate_material_width_separation(self):
        for record in self:
            record.material_width_separation = record.label_height * record.assembly_figure_x + record.h1_value + record.h2_value

    product_material = fields.Many2one(
        comodel_name='material.type',
        string='Product material',
    )

    # color_number = fields.Integer(
    #     string='Color numbers'
    # )

    amount_label_exit = fields.Integer(
        string='Amount label exit'
    )

    inner_diameter_roll = fields.Float(
        string='Inner diameter roll'
    )

    outer_diameter_roll = fields.Float(
        string='Outer diameter roll'
    )

    print_orientation_id = fields.Many2one(
        comodel_name="print.orientation",
        string="Print orientation"
    )

    image_orientation = fields.Char(
        string="Imagen",
        related="print_orientation_id.image",
    )

    product_varnish = fields.Many2one(
        comodel_name='varnish.type',
        string='Product Varnish',
    )

    product_stamping = fields.Many2one(
        comodel_name='stamping.option',
        string='Product Stamping',
    )

    serigraphy = fields.Boolean(
        string='Serigraphy',
    )

    relief = fields.Boolean(
        string='Relief',
    )

    laminated = fields.Selection(
        selection=[
            ("gloss", "Brillo"),
            ("matte", "Mate"),
        ],
        string="Laminated",
    )

    other_finishes = fields.Char(
        string='Other finishes',
    )

    preprint_comments = fields.Char(
        string='Preprint comments',
    )

    administration_comments = fields.Char(
        string='Administration Comments'
    )

    reviewers_expedition = fields.Char(
        string='Reviewers/Expedition'
    )

    regulatory_council_numbering = fields.Char(
        string='Regulatory council numbering'
    )

    color_ink_ids = fields.One2many(
        comodel_name='color.ink',
        inverse_name='product_template_id',
        string='Colors ink'
    )
