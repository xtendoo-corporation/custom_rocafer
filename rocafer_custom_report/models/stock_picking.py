from odoo import models, api

class Picking(models.Model):
    _inherit = "stock.picking"

    def do_print_picking_valued(self):
        self.write({'printed': True})
        # Albaran valorado con condiciones segun el tipo de usuario
        # return self.env.ref('stock.action_report_picking').report_action(self)
        # Albaran valorado por oca
        return self.env.ref('stock.action_report_delivery').report_action(self)

    def action_stock_picking_report_valued(self):
        return self.env.ref('rocafer_custom_report.action_stock_picking_report_valued').report_action(self)
