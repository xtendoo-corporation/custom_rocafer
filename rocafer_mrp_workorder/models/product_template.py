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


