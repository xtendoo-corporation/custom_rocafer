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
        string='X width'
    )

    assembly_figure_y = fields.Integer(
        string='Y height'
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
        default=lambda self: self.env.company.h1_value,
    )
    h2_value = fields.Float(
        string='H2 Value',
        default=lambda self: self.env.company.h2_value,
    )

    amount = fields.Integer(
        string='Amount',
    )

    linear_meters = fields.Integer(
        string='Linear meters',
        compute='_compute_meters',
        store=True
    )

    @api.depends('amount', 'assembly_figure_x')
    def _compute_meters(self):
        self.linear_meters = 0
        for record in self.filtered(lambda r: r.assembly_figure_x):
            record.linear_meters = record.amount / record.assembly_figure_x

    advance_label_separation = fields.Float(
        string='Advance label separation',
        compute='_compute_advance_label_separation',
        store=True
    )

    @api.depends('label_width', 'h1_value')
    def _compute_advance_label_separation(self):
        for record in self:
            record.advance_label_separation = record.label_width + record.h1_value

    @api.onchange('advance_label_separation')
    def _compute_printing_cylinder_id(self):
        for record in self:
            line_id = self.env['printing.cylinder.line'].search([('size', '>=', record.advance_label_separation)], limit=1, order='size asc')
            print("*" * 80)
            print(line_id)
            if line_id:
                record.printing_cylinder_id = line_id.printing_cylinder_id

    printing_cylinder_id = fields.Many2one(
        comodel_name="printing.cylinder",
        string="Máquina",
        default=_compute_printing_cylinder_id,
    )

    # z_impression_cylinder = fields.One2many(
    #     comodel_name="printing.cylinder",
    #     string="Z Cilindro imrpesión",
    #     default=_compute_printing_cylinder_id.z_impression_cylinder,
    # )
    #
    # z_magnetic_cut = fields.One2many(
    #     comodel_name="printing.cylinder",
    #     string="Z Magnético Corte",
    #     default=_compute_printing_cylinder_id.z_magnetic_cut,
    # )
    #
    # printing_cylinder_size = fields.Many2one(
    #     comodel_name="printing.cylinder",
    #     string="Cylinder size",
    #     default=_compute_printing_cylinder_id.printing_cylinder_size,
    # )

    #*****************

    material_width_separation = fields.Integer(
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

    inner_diameter_roll = fields.Integer(
        string='Inner diameter roll'
    )

    outer_diameter_roll = fields.Integer(
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
