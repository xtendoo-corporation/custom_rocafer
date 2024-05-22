# -*- coding: utf-8 -*-

from odoo.tests.common import TransactionCase


class TestProduct(TransactionCase):

    def setUp(self):
        super(TestProduct, self).setUp()
        self.product = self.env['product.template'].create({
            #CLIENTE
            'name': 'Test Product',
            'res_partner_id': 1,
            #TROQUEL
            'label_code': 'Test Label Code',
            'troquel_number': 1532,
            'assembly_figure_x': 2,
            'assembly_figure_y': 4,
            #PRODUCCION - Corregir traduccion
            'label_width': 180,
            'label_height': 60,
            'amount': 5000,
        })

    def test_troquel_figure(self):
        self.assertEqual(self.product.troquel_figure, 8, 'Troquel figure calculation is incorrect')

    def test_label_width(self):
        self.assertEqual(self.product.label_width, 180, 'Label width calculation is incorrect')

    def test_printing_cylinder_size(self):
        self.assertEqual(self.product.printing_cylinder_size, 184.15, 'Printing cylinder size calculation is incorrect')

    def test_v_value(self):
        self.assertAlmostEqual(self.product.v_value, 4.15, places=2, msg='V value calculation is incorrect')

    def test_material_width_separation(self):
        self.assertEqual(self.product.material_width_separation, 138, 'Material width separation calculation is incorrect')

    def test_h1_value(self):
        self.assertEqual(self.product.h1_value, 3, 'H1 value calculation is incorrect')

    def test_h2_value(self):
        self.assertEqual(self.product.h2_value, 15, 'H2 value calculation is incorrect')

    def test_linear_meters(self):
        self.assertEqual(self.product.linear_meters, 920.75, 'Linear meters calculation is incorrect')

