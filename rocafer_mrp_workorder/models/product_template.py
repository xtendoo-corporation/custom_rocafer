# Copyright (C) 2024 Salvador Aramis González Jiménez (<https://xtendoo.es>).
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import models, api


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    @api.model
    def default_get(self, fields_list):
        # Obtener los valores predeterminados del método original
        defaults = super(ProductTemplate, self).default_get(fields_list)

        # Obtener la ruta de fabricación
        manufacture_route = self.env.ref('mrp.route_warehouse0_manufacture').id
        # Obtener la ruta de fabricación
        mto_route = self.env.ref('stock.route_warehouse0_mto').id

        # Asegurarse de que route_ids está en los valores predeterminados
        if 'route_ids' in defaults:
            route_ids = defaults['route_ids']
        else:
            route_ids = []

        # Añadir la ruta de fabricación si no está presente
        if manufacture_route not in [route[1] for route in route_ids]:
            route_ids.append((4, manufacture_route))

        # Añadir la ruta de compra si no está presente
        if mto_route not in [route[1] for route in route_ids]:
            route_ids.append((4, mto_route))

        defaults['route_ids'] = route_ids
        return defaults

    @api.model_create_multi
    def create(self, vals_list):
        # Crear los productos
        products = super(ProductTemplate, self).create(vals_list)

        # Crear la regla de abastecimiento para cada producto creado
        for product in products:
            # self._create_replenishment_rule(product.id)
            self.env['ir.cron'].create_replenishment_rule_cron(product.id)

        print("*"*80)
        print('PRODUCTOS CREADOS')

        return products

    def _create_replenishment_rule(self, product_id):
        product = self.env['product.product'].browse(product_id)
        print("*"*80)
        print('PRODUCTO:', product)
        # Obtener el almacén predeterminado
        warehouse = self.env['stock.warehouse'].search([], limit=1)
        print("*"*80)
        print('WAREHOUSE:', warehouse)

        if warehouse:
            # Buscar si ya existe una regla de abastecimiento para este producto en el almacén
            existing_rule = product.env['stock.warehouse.orderpoint'].search([
                ('product_id', '=', product.id),
                ('warehouse_id', '=', warehouse.id)
            ], limit=1)

            print("*" * 80)
            print('REGLA DE ABASTECIMIENTO EXISTENTE:', existing_rule)

            if not existing_rule:
                # Crear una nueva regla de abastecimiento
                self.env['stock.warehouse.orderpoint'].create({
                    'product_id': product.id,
                    'location_id': warehouse.lot_stock_id.id,
                    'warehouse_id': warehouse.id,
                    'product_min_qty': 0,  # Cantidad mínima de stock (ajustar según sea necesario)
                    'product_max_qty': 0,  # Cantidad máxima de stock (ajustar según sea necesario)
                    'qty_multiple': 1,  # Múltiplo de pedido (ajustar según sea necesario)
                })
                print("*"*80)
                print('REGLA DE ABASTECIMIENTO CREADA')

            # Asegurarse de que la ruta de MTO esté en las rutas del producto
            route_mto = self.env.ref('stock.route_warehouse0_mto')
            if route_mto not in self.route_ids:
                self.write({
                    'route_ids': [(4, route_mto.id)]
                })
                print("*"*80)
                print('RUTA DE MTO AÑADIDA')
        print("*"*80)
        print('FIN DE LA CREACIÓN DE LA REGLA DE ABASTECIMIENTO')


class StockWarehouseOrderpointCron(models.Model):
    _inherit = 'ir.cron'

    @api.model
    def create_replenishment_rule_cron(self, product_id):
        print("*"*80)
        print("CRON JOB")
        self.create({
            'name': 'Create Replenishment Rule',
            'model_id': self.env.ref('product.model_product_template').id,
            'state': 'code',
            'code': f"model._create_replenishment_rule({product_id})",
            'user_id': self.env.ref('base.user_root').id,
            'interval_number': 1,
            'interval_type': 'minutes',
            'numbercall': 1,
            'doall': False,
        })

