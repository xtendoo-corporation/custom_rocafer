# Copyright (C) 2024 Salvador Aramis González Jiménez (<https://xtendoo.es>).
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import fields, models, api


class MrpProduction(models.Model):
    _inherit = "mrp.production"

    @api.model
    def create(self, vals):
        # Crear la orden de fabricación
        production = super(MrpProduction, self).create(vals)

        # Obtener un workcenter válido
        workcenter = self.env['mrp.workcenter'].search([], limit=1)
        if not workcenter:
            raise ValueError("No hay un centro de trabajo (workcenter) disponible")

        # Obtener la unidad de medida del producto
        product_uom_id = production.product_id.uom_id.id
        if not product_uom_id:
            raise ValueError("El producto a fabricar no tiene una unidad de medida (UoM) asignada")

        # Crear las workorders asociadas
        workorder_vals = [
            {
                'name': 'Fabricación',
                'production_id': production.id,  # Relaciona la workorder con la orden de fabricación creada
                'workcenter_id': workcenter.id,  # Asigna el centro de trabajo
                'product_uom_id': product_uom_id,  # Asigna la unidad de medida del producto
                'state': 'ready',
            },
            {
                'name': 'Revisión',
                'production_id': production.id,  # Relaciona la workorder con la orden de fabricación creada
                'workcenter_id': workcenter.id,  # Asigna el centro de trabajo
                'product_uom_id': product_uom_id,  # Asigna la unidad de medida del producto
                'state': 'waiting',
            }
        ]
        workorders = self.env['mrp.workorder'].create(workorder_vals)

        # Confirmar las workorders si la orden de fabricación está en un estado apropiado
        if production.state in ("confirmed", "progress", "to_close"):
            workorders._action_confirm()
        else:
            # Si la producción está en draft, cambiar el estado a confirmed
            if production.state == 'draft':
                production.state = 'confirmed'

        return production
