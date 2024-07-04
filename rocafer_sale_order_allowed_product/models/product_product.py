# Copyright 2024 Xtendoo - Salvador González

from odoo import api, models


class ProductProduct(models.Model):
    _inherit = "product.product"

    @api.model
    def _search(self, domain, offset=0, limit=None, order=None, access_rights_uid=None):
        partner_id = self._context.get('restricted_partner_id')
        if partner_id:
            domain.append(('res_partner_id', '=', partner_id))
        return super()._search(domain, offset, limit, order, access_rights_uid)
