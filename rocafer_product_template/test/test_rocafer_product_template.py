
import odoo
from odoo.tests.common import TransactionCase


class TestProduct(TransactionCase):

    def setUp(self):
        super().setUp()
        self.Product = self.env['product.template']

    def test_calculate_troquel_figure(self):
        product = self.Product.create({
            'assembly_figure_x': 5,
            'assembly_figure_y': 10,
        })
        self.assertEqual(product.troquel_figure, 50)

    def test_compute_meters(self):
        product = self.Product.create({
            'amount': 100,
            'assembly_figure_x': 10,
        })
        self.assertEqual(product.linear_meters, 10)

    def test_compute_advance_label_separation(self):
        product = self.Product.create({
            'label_width': 5.0,
            'h1_value': 2.5,
        })
        self.assertEqual(product.advance_label_separation, 7.5)

    def test_calculate_material_width_separation(self):
        product = self.Product.create({
            'label_height': 5,
            'assembly_figure_x': 10,
            'h1_value': 2.5,
            'h2_value': 2.5,
        })
        self.assertEqual(product.material_width_separation, 55)
