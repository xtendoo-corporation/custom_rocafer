from odoo import models, api

class Picking(models.Model):
    _inherit = "stock.picking"

    def do_print_picking_valued(self):
        print("*"*80)
        self.write({'printed': True})
        return self.env.ref('stock.action_report_picking').report_action(self)
