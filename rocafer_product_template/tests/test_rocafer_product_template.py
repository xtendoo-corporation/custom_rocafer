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

        })

    #buscar odoo selenium test(similar)
    #odoo tools

    def test_product_creation(self):
        self.assertEqual(self.product.name, 'Test Product', 'Product name is incorrect')

    def test_troquel_figure_calculation(self):
        self.assertEqual(self.product.troquel_figure, 7, 'Troquel figure calculation is incorrect')

    def test_printing_cylinder_size_calculation(self):
        self.product.label_width = 112
        self.product.h1_value = 100
        self.product._compute_printing_cylinder_size()
        self.assertEqual(self.product.printing_cylinder_size, 117.48, 'Printing cylinder size calculation is incorrect')

    def test_material_width_separation(self):
        self.product.printing_cylinder_size = 84.67
        self.product.assembly_figure_x = 4
        self.product.amount = 5000
        self.product._compute_meters()
        self.assertEqual(self.product.linear_meters, 423.35, 'Linear meters calculation is incorrect')
